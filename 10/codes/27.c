#include <stdio.h>
#include <stdlib.h>

#define N 1000000

int main(void)
{
    /* pmf: n = 0 black, n = 1 brown, n = 2 blue */
    double pmf[3] = {0.65, 0.25, 0.10};
    int count[3] = {0};

    srand(2025);

    /* Simulation: pick the eye colour of N students */
    for (int i = 0; i < N; i++) {
        double u = (double)rand() / ((double)RAND_MAX + 1.0);
        int n = (u < pmf[0]) ? 0 : (u < pmf[0] + pmf[1]) ? 1 : 2;
        count[n]++;
    }

    printf("x\tsimulation\tpmf\n");
    for (int n = 0; n < 3; n++)
        printf("%d\t%.4f\t\t%.2f\n", n, (double)count[n] / N, pmf[n]);

    /* save the simulated and exact pmf for plotting */
    FILE *fp = fopen("27.dat", "w");
    const char *name[3] = {"black", "brown", "blue"};
    for (int n = 0; n < 3; n++)
        fprintf(fp, "%s %.6f %.6f\n", name[n], (double)count[n] / N, pmf[n]);
    fclose(fp);

    printf("(a) Pr(blue)         : simulation %.4f, pmf %.2f\n",
           (double)count[2] / N, pmf[2]);
    printf("(b) Pr(brown, black) : simulation %.4f, pmf %.2f\n",
           (double)(count[0] + count[1]) / N, pmf[0] + pmf[1]);

    return 0;
}
