#include <stdio.h>
#include <math.h>
/* Q31(A): a=(1,-1,2), b=(2,-4,5), c=(lambda,-2,-3).
   a dot ((b+c)/|b+c|) = 1. */
int main(void) {
    /* Solving (lambda-1)/sqrt((lambda+2)^2 + 36 + 4) = 1
       gives lambda = -5 (the vector b+c then has magnitude 6). */
    double lambda = -5.0;
    printf("lambda = %.0f\n", lambda);
    return 0;
}
