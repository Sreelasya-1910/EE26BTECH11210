#include <stdio.h>

typedef struct {
    double x;
    double y;
} Point;

Point divide_segment(Point A, Point B, int numerator, int denominator)
{
    Point P;

    P.x = A.x + (numerator / (double) denominator) * (B.x - A.x);
    P.y = A.y + (numerator / (double) denominator) * (B.y - A.y);

    return P;
}

int main(void)
{
    Point A = {-2.0, 2.0};
    Point B = { 2.0, 8.0};

    for (int i = 1; i <= 3; i++)
    {
        Point P = divide_segment(A, B, i, 4);

        printf("Division point %d = (%.2f, %.2f)\n",
               i, P.x, P.y);
    }

    return 0;
}

