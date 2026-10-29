#include <stdio.h>
#include <math.h>
/* Q31(B): shortest distance between the two given parallel lines. */
int main(void) {
    /* r1=(2,-1,3)+t(1,-2,3); r2=(1,0,4)+s(3,-6,9).
       d = |(r2-r1) x v| / |v| = sqrt(3). */
    printf("Shortest distance = sqrt(3) = %.6f\n", sqrt(3.0));
    return 0;
}
