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

int main(void)
{
    /* X = 1 for a head, Y = 1 for a face card */
    Seq pX = {0, 2, {1.0 / 2.0, 1.0 / 2.0}};
    Seq pY = {0, 2, {40.0 / 52.0, 12.0 / 52.0}};

    /* S = X + Y has pmf pX * pY, and S = 2 exactly when both are 1 */
    Seq pS = convolve(pX, pY);

    for (int n = 0; n <= 2; n++)
        printf("P(S = %d) = %.6f\n", n, value_at(pS, n));

    printf("P(head and face card) = P(S = 2) = %.6f (= 3/26)\n",
           value_at(pS, 2));

    return 0;
}
