#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846

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

double norm(Vector2D a)
{
    return sqrt(dot(a, a));
}

int main(void)
{
    double angle_APB = 80.0;      /* angle between the tangents (deg) */
    double r = 2.0;               /* radius used for the plot         */

    /* Unit direction vectors of PA and PB are (-sin(phi), +-cos(phi)),
       so cos(APB) = -cos(2 phi), where phi = angle POA. */
    double cos2phi = -cos(angle_APB * PI / 180.0);
    double phi = 0.5 * acos(cos2phi);

    /* Take O at the origin and P on the x-axis: r = d cos(phi) */
    double d = r / cos(phi);

    Vector2D O = {0.0, 0.0};
    Vector2D P = {d, 0.0};
    Vector2D A = {r * cos(phi),  r * sin(phi)};
    Vector2D B = {r * cos(phi), -r * sin(phi)};

    /* Verify: radius is perpendicular to tangent, and APB = 80 deg */
    Vector2D OA = subtract(A, O), PA = subtract(A, P);
    Vector2D OB = subtract(B, O), PB = subtract(B, P);

    double check_A = dot(OA, PA);
    double check_B = dot(OB, PB);
    double apb = acos(dot(PA, PB) / (norm(PA) * norm(PB))) * 180.0 / PI;

    printf("Angle POA = %.2f degrees\n", phi * 180.0 / PI);
    printf("P = (%.4f, %.4f)\n", P.x, P.y);
    printf("A = (%.4f, %.4f)\n", A.x, A.y);
    printf("B = (%.4f, %.4f)\n", B.x, B.y);
    printf("OA.PA = %.2e, OB.PB = %.2e\n", check_A, check_B);
    printf("Angle APB from coordinates = %.2f degrees\n", apb);

    return 0;
}
