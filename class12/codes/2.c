#include <stdio.h>
/* Q2: f(x) = acos(x) + sin(x). Domain is [-1, 1]. */
int main(void) {
    double x;
    printf("Enter x: ");
    if (scanf("%lf", &x) != 1) return 1;
    if (x >= -1.0 && x <= 1.0)
        printf("x is in the domain [-1, 1].\n");
    else
        printf("x is outside the domain [-1, 1].\n");
    return 0;
}
