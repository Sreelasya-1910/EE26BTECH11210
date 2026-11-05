#include <stdio.h>
/* Q27(A): Solve 2x+5y=1 and 3x+2y=7 by Cramer's rule. */
int main(void) {
    double D = 2*2 - 5*3;
    double Dx = 1*2 - 5*7;
    double Dy = 2*7 - 1*3;
    double x = Dx/D, y = Dy/D;
    printf("Common point: (%.2f, %.2f)\n", x, y); /* (3,-1) */
    return 0;
}
