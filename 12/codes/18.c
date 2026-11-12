#include <stdio.h>
#include <stdlib.h>

#define N 1000000

int main(void)
{
    int count[2][2] = {{0}};      /* count[x][y]: x = head, y = face card */
    srand(2025);

    for (int i = 0; i < N; i++) {
        int head = (rand() % 2 == 0);            /* toss a coin           */
        int card = rand() % 52;                  /* draw a card           */
        int face = (card % 13 >= 10);            /* J, Q, K: 12 of 52     */
        count[head][face]++;
    }

    /* pmf of X (head = 1): 1/2, 1/2;  pmf of Y (face = 1): 10/13, 3/13.
       The trials are independent, so p(x, y) = p_X(x) p_Y(y) */
    double pX[2] = {1.0 / 2.0, 1.0 / 2.0};
    double pY[2] = {40.0 / 52.0, 12.0 / 52.0};

    /* save the simulated and exact joint pmf for plotting */
    FILE *fp = fopen("18.dat", "w");
    for (int x = 0; x < 2; x++)
        for (int y = 0; y < 2; y++)
            fprintf(fp, "(%d,%d) %.6f %.6f\n", x, y,
                    (double)count[x][y] / N, pX[x] * pY[y]);
    fclose(fp);

    printf("P(head and face card): simulation %.4f, pmf %.4f (= 3/26)\n",
           (double)count[1][1] / N, pX[1] * pY[1]);

    return 0;
}
