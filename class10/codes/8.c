
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

double dot(Vector2D a, Vector2D b)
{
    return a.x * b.x + a.y * b.y;
}

int main(void)
{
    Vector2D A = {0.0, 2.0};
    Vector2D B = {4.0, 0.0};

    /* Diagonal vector AB */
    Vector2D diagonal = subtract(B, A);

    /* Squared length = diagonal dot diagonal */
    double squared_length = dot(diagonal, diagonal);

    printf("Diagonal vector AB = (%.2f, %.2f)\n",
           diagonal.x, diagonal.y);

    printf("Square of diagonal length = %.2f\n",
           squared_length);

    return 0;
}

