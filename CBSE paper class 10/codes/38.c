#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846

typedef struct {
    double height;
    double angleP;
    double angleQ;
} Lighthouse;

double toRadians(double degrees) {
    return degrees * PI / 180.0;
}

double horizontalDistance(double height, double angle) {
    return height / tan(toRadians(angle));
}

double shipDistance(Lighthouse *light) {
    double p = horizontalDistance(light->height, light->angleP);
    double q = horizontalDistance(light->height, light->angleQ);

    return p - q;
}

double speedKmph(double distanceMetres, double timeMinutes) {
    double distanceKm = distanceMetres / 1000.0;
    double timeHours = timeMinutes / 60.0;

    return distanceKm / timeHours;
}

int main(void) {
    Lighthouse light = {50.0, 30.0, 45.0};

    double distanceQ = horizontalDistance(
        light.height, light.angleQ
    );

    double distanceP = horizontalDistance(
        light.height, light.angleP
    );

    double distancePQ = shipDistance(&light);

    double speed = speedKmph(distanceQ, 10.0);

    printf("Distance QA = %.2f m\n", distanceQ);
    printf("Distance PA = %.2f m\n", distanceP);
    printf("Distance travelled PQ = %.2f m\n", distancePQ);
    printf("Speed from Q to A = %.2f km/h\n", speed);

    return 0;
}

