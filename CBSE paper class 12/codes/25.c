#include <stdio.h>
/* Q25(A): X takes 0,1,2,3 with frequencies 2,3,4,1 out of 10 blocks. */
int main(void) {
    int x[] = {0,1,2,3};
    int frequency[] = {2,3,4,1};
    double mean = 0.0;
    puts("x\tP(X=x)");
    for (int i=0;i<4;i++) {
        double p = frequency[i]/10.0;
        printf("%d\t%.2f\n", x[i], p);
        mean += x[i]*p;
    }
    printf("Mean = %.2f\n", mean); /* 1.4 */
    return 0;
}
