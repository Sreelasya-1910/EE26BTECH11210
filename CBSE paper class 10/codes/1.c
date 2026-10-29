
#include <stdio.h>


int main(void)
{
    const double tangent_angle = 80.0;
    const double right_angle = 90.0;
    const double full_angle = 360.0;

    double angle_AOB;
    double angle_POA;

    /* Angle sum of quadrilateral AOBP */
    angle_AOB = full_angle
              - tangent_angle
              - 2.0 * right_angle;

    /* OP bisects angle AOB */
    angle_POA = angle_AOB / 2.0;

    printf("Angle APB = %.2f degrees\n", tangent_angle);
    printf("Angle AOB = %.2f degrees\n", angle_AOB);
    printf("Angle POA = %.2f degrees\n", angle_POA);


    return 0;
}

