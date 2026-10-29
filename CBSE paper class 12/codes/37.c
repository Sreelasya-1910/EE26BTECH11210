#include <stdio.h>
/* Q37: Spherical/camphor model. This generic script calculates r(t)=r0-k*t
   after k is obtained from a supplied radius measurement. */
int main(void) {
    double r0 = 5.0, t_measure = 1.0, r_measure = 3.0;
    double k = (r0-r_measure)/t_measure;
    double target = 1.0;
    double time_target = (r0-target)/k;
    printf("Rate constant k = %.2f radius-units/hour\n", k);
    printf("Time to reach radius %.2f = %.2f hours\n", target, time_target);
    return 0;
}
