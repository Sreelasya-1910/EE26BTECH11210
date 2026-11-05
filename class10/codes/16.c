#include <stdio.h>
#define PI 3.14159265358979323846

int main(void)
{
    double radius = 36.0;
    double area = 54.0 * PI;

    double arc_length = (2.0 * area) / radius;

    printf("Radius = %.2f cm\n", radius);
    printf("Sector area = %.2f cm^2\n", area);
    printf("Arc length = %.6f cm\n", arc_length);

    return 0;
}

