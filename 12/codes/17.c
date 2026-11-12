#include <stdio.h>
#include <stdlib.h>

#define N 1000000

int main(void)
{
    /* Outcome cells: 0 = A and B (4/7), 1 = A' and B (1/7), 2 = not B (2/7) */
    double pmf[3] = {4.0 / 7.0, 1.0 / 7.0, 2.0 / 7.0};
    int count[3] = {0};

    srand(2025);

    for (int i = 0; i < N; i++) {
        double u = (double)rand() / ((double)RAND_MAX + 1.0);
        int cell = (u < pmf[0]) ? 0 : (u < pmf[0] + pmf[1]) ? 1 : 2;
        count[cell]++;
    }

    /* save the simulated and exact pmf for plotting */
    FILE *fp = fopen("17.dat", "w");
    const char *name[3] = {"A^B", "A'^B", "B'"};
    for (int c = 0; c < 3; c++)
        fprintf(fp, "%s %.6f %.6f\n", name[c], (double)count[c] / N, pmf[c]);
    fclose(fp);

    double P_B   = (double)(count[0] + count[1]) / N;
    double P_AcB = (double)count[1] / N;

    printf("P(B)        : simulation %.4f, pmf %.4f\n", P_B, 5.0 / 7.0);
    printf("P(A' and B) : simulation %.4f, pmf %.4f\n", P_AcB, 1.0 / 7.0);
    printf("P(A' | B)   : simulation %.4f, pmf %.4f\n", P_AcB / P_B, 1.0 / 5.0);

    return 0;
}
