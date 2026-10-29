#include <stdio.h>
/*
Q17 as printed states P(A)=1/7, P(B)=5/7, P(A intersection B)=4/7.
These values are inconsistent because P(A intersection B) cannot exceed P(A).
This program checks that probability data are valid before using conditional probability.
*/
int main(void) {
    double pA = 1.0/7.0, pB = 5.0/7.0, pAB = 4.0/7.0;
    if (pAB > pA || pAB > pB || pA < 0 || pA > 1 || pB < 0 || pB > 1) {
        puts("The given probabilities are inconsistent; conditional probability cannot be computed.");
        return 0;
    }
    printf("P(A-bar | B) = (P(B)-P(A intersection B))/P(B) = %.6f\n",
           (pB-pAB)/pB);
    return 0;
}
