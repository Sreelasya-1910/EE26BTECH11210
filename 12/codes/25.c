#include <stdio.h>
#include <stdlib.h>

#define N 1000000

int main(void)
{
    /* The ten blocks: two marked 0, three marked 1, four marked 2, one marked 3 */
    int block[10] = {0, 0, 1, 1, 1, 2, 2, 2, 2, 3};
    int count[4] = {0};
    double sum = 0.0;

    srand(2025);

    for (int i = 0; i < N; i++) {
        int x = block[rand() % 10];     /* draw a block at random */
        count[x]++;
        sum += x;
    }

    double pmf[4] = {0.2, 0.3, 0.4, 0.1};
    /* save the simulated and exact pmf for plotting */
    FILE *fp = fopen("25.dat", "w");
    for (int x = 0; x < 4; x++)
        fprintf(fp, "%d %.6f %.6f\n", x, (double)count[x] / N, pmf[x]);
    fclose(fp);

    double mean = 0.0;

    printf("x\tsimulation\tpmf\n");
    for (int x = 0; x < 4; x++) {
        printf("%d\t%.4f\t\t%.2f\n", x, (double)count[x] / N, pmf[x]);
        mean += x * pmf[x];
    }

    printf("Mean: simulation %.4f, sum of x p(x) = %.2f\n", sum / N, mean);

    return 0;
}
