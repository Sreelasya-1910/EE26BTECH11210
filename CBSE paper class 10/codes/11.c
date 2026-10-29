#include <stdio.h>
#include <math.h>

typedef struct {
    double x;
    double y;
} Vector2D;

Vector2D subtract(Vector2D a, Vector2D b)
{
    Vector2D result = {a.x - b.x, a.y - b.y};
    return result;
}

double dot(Vector2D a, Vector2D b)
{
    return a.x * b.x + a.y * b.y;
}

double squared_length(Vector2D v)
{
    return dot(v, v);
}

int main(void)
{
    double BC = 16.0;
    double DC = 4.0;

    Vector2D B = {0.0, 0.0};
    Vector2D C = {BC, 0.0};

    double BD = BC - DC;
    Vector2D D = {BD, 0.0};

    /*
       Let A = (BD, h).
       Since AB and AC are perpendicular:
       (B - A) dot (C - A) = 0.
    */

    double h_squared = BD * DC;

    Vector2D A = {BD, sqrt(h_squared)};

    Vector2D AB = subtract(B, A);
    Vector2D AC = subtract(C, A);

    double perpendicular_check = dot(AB, AC);
    double AC_squared = squared_length(AC);
    double AC_length = sqrt(AC_squared);

    printf("Coordinates of D: (%.2f, %.2f)\n",
           D.x, D.y);

    printf("Coordinates of A: (%.4f, %.4f)\n",
           A.x, A.y);

    printf("AB dot AC = %.6f\n",
           perpendicular_check);

    printf("AC squared = %.2f cm^2\n",
           AC_squared);

    printf("AC = %.2f cm\n", AC_length);

    return 0;
}

