#include <stdio.h>

#define MAXLEN 32

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

int main(void)
{
    /* pmf of a fair die: p[n] = (1/6)(u[n-1] - u[n-7]) */
    Seq p = {1, 6, {1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6}};

    /* m[n] = 1 if n is not a factor of 36, else 0 */
    Seq m = {1, 6, {0}};
    for (int n = 1; n <= 6; n++)
        m.v[n - 1] = (36 % n != 0) ? 1.0 : 0.0;

    /* h[n] = m[-n], defined for n = -6, ..., -1 */
    Seq h = {-6, 6, {0}};
    for (int n = -6; n <= -1; n++)
        h.v[n - h.n0] = value_at(m, -n);

    /* Z-transform of a convolution is a product; the coefficient of
       z^0 in P(z)H(z) is (p * h)[0] */
    Seq y = convolve(p, h);

    printf("m[n], n = 1..6 : ");
    for (int n = 1; n <= 6; n++)
        printf("%.0f ", value_at(m, n));

    printf("\n(p*h)[n] for n = %d..%d:\n", y.n0, y.n0 + y.len - 1);
    for (int i = 0; i < y.len; i++)
        printf("  n = %3d : %.6f\n", y.n0 + i, y.v[i]);

    printf("\nPr(E) = (p*h)[0] = %.6f (= 1/6)\n", value_at(y, 0));

    return 0;
}
