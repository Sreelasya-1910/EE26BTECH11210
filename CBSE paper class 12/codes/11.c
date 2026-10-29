#include <stdio.h>
#include <math.h>
/* Q11: f(x)=2x-sin(x), f'(x)=2-cos(x) >= 1, so f is increasing on R. */
int main(void) {
    double x, derivative;
    printf("Enter x in radians: ");
    if (scanf("%lf", &x) != 1) return 1;
    derivative = 2.0 - cos(x);
    if (derivative < 0.0) puts("Decreasing at this point.");
    else if (derivative > 0.0) puts("Increasing at this point.");
    else puts("Derivative is zero at this point.");
    puts("Since 2-cos(x) >= 1 for all real x, f is strictly increasing on R.");
    return 0;
}
