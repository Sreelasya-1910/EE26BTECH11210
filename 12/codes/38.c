#include <stdio.h>
#include <stdlib.h>

#define N 1000000

int main(void)
{
    double p[3] = {0.70, 0.20, 0.10};    /* P(A_1), P(A_2), P(A_3)  */
    double d[3] = {0.25, 0.35, 0.50};    /* P(D | A_i)              */

    long count[3][2] = {{0}};            /* count[i][1]: A_i and D, count[i][0]: A_i and D' */

    srand(2025);

    for (int i = 0; i < N; i++) {
        double u = (double)rand() / ((double)RAND_MAX + 1.0);
        int cat = (u < p[0]) ? 0 : (u < p[0] + p[1]) ? 1 : 2;

        double v = (double)rand() / ((double)RAND_MAX + 1.0);
        int disease = (v < d[cat]);

        count[cat][disease]++;
    }

    /* save the simulated and exact joint pmf for plotting */
    FILE *fp = fopen("38.dat", "w");
    for (int c = 0; c < 3; c++) {
        fprintf(fp, "A%d^D %.6f %.6f\n",  c + 1, (double)count[c][1] / N, p[c] * d[c]);
        fprintf(fp, "A%d^D' %.6f %.6f\n", c + 1, (double)count[c][0] / N, p[c] * (1 - d[c]));
    }
    fclose(fp);

    long count_D  = count[0][1] + count[1][1] + count[2][1];
    long count_Dc = count[0][0] + count[1][0] + count[2][0];

    double P_D  = p[0] * d[0] + p[1] * d[1] + p[2] * d[2];
    double P_Dc = 1.0 - P_D;

    printf("P(D)        : simulation %.4f, pmf %.4f\n", (double)count_D / N, P_D);
    printf("P(D')       : simulation %.4f, pmf %.4f\n", (double)count_Dc / N, P_Dc);
    printf("P(A1 | D')  : simulation %.4f, pmf %.4f (= 35/47)\n",
           (double)count[0][0] / count_Dc, p[0] * (1 - d[0]) / P_Dc);

    return 0;
}
