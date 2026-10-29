#include <stdio.h>
/* Q30: Minimize Z=18x+10y subject to 4x+y>=20, 2x+3y>=30, x,y>=0.
   The intersection is (3,8), Z=134. */
int main(void) {
    double det = 4*3 - 1*2;
    double x = (20*3 - 1*30)/det;
    double y = (4*30 - 20*2)/det;
    double z = 18*x + 10*y;
    printf("Intersection: (%.2f, %.2f)\nMinimum Z = %.2f\n", x, y, z);
    return 0;
}
