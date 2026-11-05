#include <stdio.h>

#define MAXLEN 16

/* A finite sequence x[n], n = n0, n0+1, ..., n0+len-1 */
typedef struct {
    int n0;
    int len;
    double v[MAXLEN];
} Seq;

/* y[n] = sum_k a[k] b[n-k] */
Seq convolve(Seq a, Seq b)
{
    Seq y = {a.n0 + b.n0, a.len + b.len - 1, {0.0}};

    for (int i = 0; i < a.len; i++)
        for (int j = 0; j < b.len; j++)
            y.v[i + j] += a.v[i] * b.v[j];

    return y;
}

double value_at(Seq x, int n)
{
    int i = n - x.n0;
    return (i >= 0 && i < x.len) ? x.v[i] : 0.0;
}

/* h[n] = m[-n] */
Seq reverse(Seq m)
{
    Seq h = {-(m.n0 + m.len - 1), m.len, {0.0}};

    for (int i = 0; i < m.len; i++)
        h.v[i] = m.v[m.len - 1 - i];

    return h;
}

int main(void)
{
    /* n = 0: Black, n = 1: Brown, n = 2: Blue
       p[n] = 0.65 d[n] + 0.25 d[n-1] + 0.10 d[n-2] */
    Seq p = {0, 3, {0.65, 0.25, 0.10}};

    /* Event (a): blue            -> m[n] = d[n-2]        */
    Seq m_a = {2, 1, {1.0}};

    /* Event (b): brown or black  -> m[n] = d[n] + d[n-1] */
    Seq m_b = {0, 2, {1.0, 1.0}};

    Seq y_a = convolve(p, reverse(m_a));
    Seq y_b = convolve(p, reverse(m_b));

    printf("(a) Blue eyes           : (p*h)[0] = %.2f\n", value_at(y_a, 0));
    printf("(b) Brown or black eyes : (p*h)[0] = %.2f\n", value_at(y_b, 0));

    return 0;
}
