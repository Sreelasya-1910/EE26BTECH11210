#include <stdio.h>
/* For an n x n matrix: |adj(A)| = |A|^(n-1). Here n=3, |A|=5. */
double det3(const double m[3][3]) {
    return m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
         - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
         + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]);
}
int main(void) {
    const double A[3][3] = {{5,0,0},{0,1,0},{0,0,1}};
    double d = det3(A);
    printf("|adj(A)| = |A|^2 = %.0f\n", d*d); /* 25 */
    return 0;
}
