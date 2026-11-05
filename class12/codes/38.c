#include <stdio.h>

#define MAXLEN 16

/* A finite sequence x[n], n = n0, ..., n0+len-1 */
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
    /* n = 0, 1, 2 : good, average, poor health */
    Seq p  = {0, 3, {0.70, 0.20, 0.10}};     /* P(A_n+1)       */
    Seq d  = {0, 3, {0.25, 0.35, 0.50}};     /* P(D | A_n+1)   */
    Seq dc = {0, 3, {0.75, 0.65, 0.50}};     /* P(D' | A_n+1)  */
    Seq p1 = {0, 1, {0.70}};                 /* p[n] restricted to A_1 */

    /* P(D) = (p * h)[0] with h[n] = d[-n] */
    double P_D  = value_at(convolve(p, reverse(d)), 0);

    /* P(D') and P(A_1 and D') */
    double P_Dc = value_at(convolve(p,  reverse(dc)), 0);
    double P_A1Dc = value_at(convolve(p1, reverse(dc)), 0);

    printf("P(D)        = %.4f\n", P_D);
    printf("P(D')       = %.4f\n", P_Dc);
    printf("P(A1 and D')= %.4f\n", P_A1Dc);
    printf("P(A1 | D')  = %.6f (= 35/47)\n", P_A1Dc / P_Dc);

    return 0;
}
