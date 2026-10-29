#include <stdio.h>
/* Standard C has no built-in determinant function. */
double det3(const double m[3][3]) {
    return m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
         - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
         + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]);
}
int main(void) {
    const double A[3][3] = {{3,0,0},{0,1,0},{0,0,1}};
    const double B[3][3] = {{5,0,0},{0,1,0},{0,0,1}};
    double detA = det3(A), detB = det3(B);
    printf("|2AB| = 2^3 |A||B| = %.0f\n", 8.0*detA*detB); /* 120 */
    return 0;
}
