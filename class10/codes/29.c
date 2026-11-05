#include <stdio.h>

int main(void)
{
    double tangent_angle = 110.0;

    /* Angle CBA: supplementary to the given obtuse angle */
    double angle_CBA = 180.0 - tangent_angle;

    /* Since AB is a diameter, angle BCA = 90 degrees */
    double angle_BCA = 90.0;

    /* Triangle ABC: calculate angle BAC */
    double angle_BAC = 180.0 - angle_BCA - angle_CBA;

    /* OA = OC, so triangle AOC is isosceles.
       Angle OAC = angle BAC.
       Therefore, angle OCA = angle BAC.
    */
    double angle_OCA = angle_BAC;

    /* Angle BCO = angle BCA - angle OCA */
    double angle_BCO = angle_BCA - angle_OCA;

    printf("Angle CBA = %.2f degrees\n", angle_CBA);
    printf("Angle BCO = %.2f degrees\n", angle_BCO);

    return 0;
}

