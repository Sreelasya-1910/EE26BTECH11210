#include <stdio.h>
#include <math.h>

#define R 2
#define C 3
#define EPS 1e-9

void print_matrix(double M[R][C])
{
    for (int i = 0; i < R; i++)
        printf("  [ %9.4f %9.4f | %9.2f ]\n", M[i][0] + 0.0, M[i][1] + 0.0, M[i][2] + 0.0);
    printf("\n");
}

/* rank = number of non-zero rows after row reduction.
   Only the first `cols` columns are considered. */
int rank_of(double M[R][C], int cols)
{
    double T[R][C];
    int rank = 0;

    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            T[i][j] = M[i][j];

    for (int col = 0; col < cols && rank < R; col++) {
        int piv = rank;
        for (int i = rank; i < R; i++)
            if (fabs(T[i][col]) > fabs(T[piv][col]))
                piv = i;

        if (fabs(T[piv][col]) < EPS)
            continue;

        for (int j = 0; j < C; j++) {
            double t = T[rank][j];
            T[rank][j] = T[piv][j];
            T[piv][j] = t;
        }

        for (int i = rank + 1; i < R; i++) {
            double f = T[i][col] / T[rank][col];
            for (int j = 0; j < C; j++)
                T[i][j] -= f * T[rank][j];
        }
        rank++;
    }
    return rank;
}

int main(void)
{
    /* 0.10 x + 0.15 y = 1900
       0.15 x + 0.10 y = 2100  (augmented matrix [A | b]) */
    double M[R][C] = {{0.10, 0.15, 1900.0},
                      {0.15, 0.10, 2100.0}};

    printf("Augmented matrix:\n");
    print_matrix(M);

    printf("rank(A) = %d, rank([A|b]) = %d\n\n", rank_of(M, 2), rank_of(M, 3));

    /* R1 <- R1 / 0.10 */
    double f = M[0][0];
    for (int j = 0; j < C; j++) M[0][j] /= f;
    printf("R1 <- R1/0.10:\n");
    print_matrix(M);

    /* R2 <- R2 - 0.15 R1 */
    f = M[1][0];
    for (int j = 0; j < C; j++) M[1][j] -= f * M[0][j];
    printf("R2 <- R2 - 0.15 R1:\n");
    print_matrix(M);

    /* R2 <- R2 / (-0.125) */
    f = M[1][1];
    for (int j = 0; j < C; j++) M[1][j] /= f;
    printf("R2 <- R2/(-0.125):\n");
    print_matrix(M);

    /* R1 <- R1 - 1.5 R2 */
    f = M[0][1];
    for (int j = 0; j < C; j++) M[0][j] -= f * M[1][j];
    printf("R1 <- R1 - 1.5 R2:\n");
    print_matrix(M);

    printf("Amount lent at 10%% = Rs. %.2f\n", M[0][2]);
    printf("Amount lent at 15%% = Rs. %.2f\n", M[1][2]);

    return 0;
}
