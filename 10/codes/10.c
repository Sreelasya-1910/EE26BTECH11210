#include <stdio.h>
#include <stdlib.h>

#define N 1000000

int main(void)
{
    int count[7] = {0};          /* count[x] = number of throws showing x */
    int favourable = 0;

    srand(2025);

    for (int i = 0; i < N; i++) {
        int x = (int)(6.0 * rand() / (RAND_MAX + 1.0)) + 1;  /* one throw of a fair die */
        count[x]++;

        if (36 % x != 0)         /* x is NOT a factor of 36 */
            favourable++;
    }

    printf("x\tp(x) from simulation\tp(x) = 1/6\n");
    for (int x = 1; x <= 6; x++)
        printf("%d\t%.4f\t\t\t%.4f\n", x, (double)count[x] / N, 1.0 / 6.0);

    /* save the simulated and exact pmf for plotting */
    FILE *fp = fopen("10.dat", "w");
    for (int x = 1; x <= 6; x++)
        fprintf(fp, "%d %.6f %.6f\n", x, (double)count[x] / N, 1.0 / 6.0);
    fclose(fp);

    printf("\nPr(not a factor of 36) from simulation = %.4f\n",
           (double)favourable / N);
    printf("Pr(not a factor of 36) from the pmf    = %.4f\n", 1.0 / 6.0);

    return 0;
}
