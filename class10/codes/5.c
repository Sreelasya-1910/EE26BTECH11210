#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846

int main(void)
{
    double sine_value = sqrt(3.0) / 2.0;

    /* asin() returns radians */
    double angle_radians = asin(sine_value);

    /* Convert radians to degrees */
    double angle_degrees = angle_radians * 180.0 / PI;

    double theta = angle_degrees / 4.0;
    double result = theta / 3.0;

    printf("4 * theta = %.2f degrees\n", angle_degrees);
    printf("theta = %.2f degrees\n", theta);
    printf("theta / 3 = %.2f degrees\n", result);

    return 0;
}
