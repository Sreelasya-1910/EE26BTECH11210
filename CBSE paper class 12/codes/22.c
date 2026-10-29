#include <stdio.h>
/* Q22: A=[[2,3],[-1,2]]. Verify A^2 - 4A + 7I = 0 entrywise. */
int main(void) {
    int A[2][2] = {{2,3},{-1,2}};
    int A2[2][2];
    int ok = 1;
    for (int i=0;i<2;i++)
        for (int j=0;j<2;j++) {
            A2[i][j] = 0;
            for (int k=0;k<2;k++) A2[i][j] += A[i][k]*A[k][j];
            int value = A2[i][j] - 4*A[i][j] + (i==j ? 7 : 0);
            if (value != 0) ok = 0;
        }
    puts(ok ? "Verified: A^2 - 4A + 7I = 0." : "Identity not verified.");
    return 0;
}
