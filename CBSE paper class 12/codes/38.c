#include <stdio.h>
/* Q38: Bayes/PMF mapping using the previously stated group proportions and rates.
   Check these values against the paper before submitting. */
int main(void) {
    double pGood=0.7, pAverage=0.2, pPoor=0.1;
    double dGood=0.25, dAverage=0.35, dPoor=0.50;
    double pDisease = pGood*dGood + pAverage*dAverage + pPoor*dPoor;
    double pAverageNoDisease = pAverage*(1.0-dAverage);
    double pNoDisease = 1.0-pDisease;
    printf("P(disease) = %.4f\n", pDisease);
    printf("P(average | no disease) = %.6f\n", pAverageNoDisease/pNoDisease);
    return 0;
}
