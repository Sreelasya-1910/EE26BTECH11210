#include <stdio.h>

#define N 4

int main(void)
{
    /* p[n] = P(X = n), n = 0, 1, 2, 3 */
    double p[N] = {2.0 / 10, 3.0 / 10, 4.0 / 10, 1.0 / 10};

    /* P(z) = sum p[n] z^(-n) and -dP/dz = sum n p[n] z^(-n-1) */
    double z = 1.0;
    double P = 0.0, minus_dP = 0.0, zk = 1.0;   /* zk = z^(-n) */

    for (int n = 0; n < N; n++) {
        P += p[n] * zk;
        minus_dP += n * p[n] * zk / z;
        zk /= z;
    }

    printf("x\tP(X=x)\n");
    for (int n = 0; n < N; n++)
        printf("%d\t%.2f\n", n, p[n]);

    printf("P(1)   = %.2f\n", P);
    printf("Mean E[X] = -P'(1) = %.2f\n", minus_dP);

    return 0;
}
