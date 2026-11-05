#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846

typedef struct {
    double x;
    double y;
} Vector2D;

Vector2D add(Vector2D a, Vector2D b)
{
    Vector2D r = {a.x + b.x, a.y + b.y};
    return r;
}

Vector2D subtract(Vector2D a, Vector2D b)
{
    Vector2D r = {a.x - b.x, a.y - b.y};
    return r;
}

Vector2D scale(Vector2D v, double k)
{
    Vector2D r = {k * v.x, k * v.y};
    return r;
}

double norm(Vector2D v)
{
    return sqrt(v.x * v.x + v.y * v.y);
}

/* Point where the line of sight B + lambda*m meets the ground y = 0:
   e2^T (B + lambda m) = 0  =>  lambda = -(e2^T B)/(e2^T m) */
Vector2D ground_point(Vector2D B, Vector2D m)
{
    double lambda = -B.y / m.y;
    return add(B, scale(m, lambda));
}

int main(void)
{
    Vector2D A = {0.0, 0.0};
    Vector2D B = {0.0, 50.0};

    double thP = 30.0 * PI / 180.0;   /* angle of depression of P */
    double thQ = 45.0 * PI / 180.0;   /* angle of depression of Q */

    /* direction vectors of the lines of sight from B */
    Vector2D mP = {cos(thP), -sin(thP)};
    Vector2D mQ = {cos(thQ), -sin(thQ)};

    Vector2D P = ground_point(B, mP);
    Vector2D Q = ground_point(B, mQ);

    double QA = norm(subtract(Q, A));
    double PA = norm(subtract(P, A));
    double PQ = norm(subtract(P, Q));
    double speed = (QA / 1000.0) / (10.0 / 60.0);   /* km/h */

    printf("P = (%.4f, %.4f)\n", P.x, P.y);
    printf("Q = (%.4f, %.4f)\n", Q.x, Q.y);
    printf("QA = %.2f m\n", QA);
    printf("PA = %.2f m\n", PA);
    printf("PQ = %.2f m\n", PQ);
    printf("Speed from Q to A = %.2f km/h\n", speed);

    return 0;
}
