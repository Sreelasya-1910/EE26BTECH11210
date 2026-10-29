#include <stdio.h>

typedef struct {
    double x;
    double y;
} Vector2D;

Vector2D subtract(Vector2D a, Vector2D b)
{
    Vector2D result = {a.x - b.x, a.y - b.y};
    return result;
}

Vector2D add(Vector2D a, Vector2D b)
{
    Vector2D result = {a.x + b.x, a.y + b.y};
    return result;
}

Vector2D scale(Vector2D v, double k)
{
    Vector2D result = {k * v.x, k * v.y};
    return result;
}

int main(void)
{
    Vector2D P = {-1.0, 5.0};
    Vector2D Q = { 5.0, 2.0};

    double m = 2.0;
    double n = 1.0;

    /* Displacement vector from P to Q */
    Vector2D PQ = subtract(Q, P);

    /* R = P + [m/(m+n)] * PQ */
    double t = m / (m + n);

    Vector2D R = add(P, scale(PQ, t));

    printf("Displacement PQ = (%.2f, %.2f)\n",
           PQ.x, PQ.y);

    printf("Position vector R = (%.2f, %.2f)\n",
           R.x, R.y);

    printf("Answer: Option C (3, 3)\n");

    return 0;
}
