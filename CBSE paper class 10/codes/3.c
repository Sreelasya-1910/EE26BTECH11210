#include <stdio.h>
#include <math.h>

int main(void)
{
    const double volume1 = 8.0;
    const double volume2 = 125.0;

    double side_ratio;
    double surface_ratio;

    /* Find the ratio of side lengths */
    side_ratio = cbrt(volume1 / volume2);

    /* Surface area is proportional to side length squared */
    surface_ratio = side_ratio * side_ratio;

    printf("Ratio of side lengths = %.2f : 1\n",
           side_ratio);

    printf("Ratio of surface areas = %.0f : %.0f\n",
           4.0, 25.0);



    return 0;
}
