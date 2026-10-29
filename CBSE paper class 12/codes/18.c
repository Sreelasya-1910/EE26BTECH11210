#include <stdio.h>
/* Q18: P(head and face card) = P(head)*P(face card) = (1/2)*(12/52)=3/26. */
int main(void) {
    double pHead = 1.0/2.0;
    double pFace = 12.0/52.0;
    double pBoth = pHead*pFace;
    printf("P(head and face card) = %.0f/%.0f = %.6f\n", 3.0, 26.0, pBoth);
    return 0;
}
