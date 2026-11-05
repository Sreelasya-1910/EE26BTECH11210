#include <stdio.h>

int main(void)
{
    const double pi = 3.14159265358979323846;

    /* Dimensions of the cone */
    double cone_radius = 5.0;
    double cone_height = 8.0;

    /* Radius of each spherical lead shot */
    double shot_radius = 0.5;

    /* Volume of water initially in the cone */
    double cone_volume =
        (1.0 / 3.0) * pi
        * cone_radius * cone_radius
        * cone_height;

    /* One-fourth of the water flows out */
    double overflow_volume = cone_volume / 4.0;

    /* Volume of one spherical lead shot */
    double shot_volume =
        (4.0 / 3.0) * pi
        * shot_radius * shot_radius * shot_radius;

    /* Number of shots = overflow volume / volume per shot */
    double number_of_shots = overflow_volume / shot_volume;

    printf("Volume of cone = %.4f cm^3\n", cone_volume);
    printf("Overflow volume = %.4f cm^3\n", overflow_volume);
    printf("Volume of one shot = %.4f cm^3\n", shot_volume);
    printf("Number of lead shots = %.0f\n", number_of_shots);

    return 0;
}

