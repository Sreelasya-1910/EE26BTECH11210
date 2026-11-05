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
    double pA = 1.0 / 7.0, pB = 5.0 / 7.0, pAB = 4.0 / 7.0;

    if (pAB > pA)
        puts("Warning: P(A and B) > P(A), the printed data are inconsistent.");

    /* The two ways B can occur: n = 0 is (A and B), n = 1 is (A' and B) */
    Seq p = {0, 2, {pAB, pB - pAB}};

    Seq m_B   = {0, 2, {1.0, 1.0}};   /* indicator of B        */
    Seq m_AcB = {1, 1, {1.0}};        /* indicator of A' and B */

    double P_B   = value_at(convolve(p, reverse(m_B)),   0);
    double P_AcB = value_at(convolve(p, reverse(m_AcB)), 0);

    printf("P(B)        = %.6f\n", P_B);
    printf("P(A' and B) = %.6f\n", P_AcB);
    printf("P(A' | B)   = %.6f\n", P_AcB / P_B);

    return 0;
}
