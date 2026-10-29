#include <stdio.h>
#include <math.h>

typedef struct {
    double x;
    double y;
} Vector2D;

Vector2D midpoint(Vector2D P, Vector2D Q)
{
    Vector2D M = {
        (P.x + Q.x) / 2.0,
        (P.y + Q.y) / 2.0
    };

    return M;
}

int main(void)
{
    /* Given points: P = (a, 4), Q = (2, 2b) */
    Vector2D P = {0.0, 4.0};
    Vector2D Q = {2.0, 0.0};

    Vector2D M = {2.0, 6.0};

    /* From midpoint coordinates:
       (a + 2)/2 = 2  => a = 2
       (4 + 2b)/2 = 6 => b = 4
    */
    P.x = 2.0 * M.x - Q.x;
    Q.y = 2.0 * M.y - P.y;

    Vector2D calculated_midpoint = midpoint(P, Q);

    double a = P.x;
    double b = Q.y / 2.0;

    printf("Point P = (%.2f, %.2f)\n", P.x, P.y);
    printf("Point Q = (%.2f, %.2f)\n", Q.x, Q.y);
    printf("Calculated midpoint = (%.2f, %.2f)\n",
           calculated_midpoint.x, calculated_midpoint.y);
    printf("a = %.2f, b = %.2f\n", a, b);
    printf("a + b = %.2f\n", a + b);

    return 0;
}
