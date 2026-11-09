
#include <stdio.h>
#include <math.h>

double f(double y)
{
    return 21.0 * y * y - 11.0 * y - 2.0;
}

double df(double y)
{
    return 42.0 * y - 11.0;
}

double newton_raphson(double initial, double tolerance)
{
    double y = initial;

    for (int i = 0; i < 100; i++)
    {
        double derivative = df(y);

        if (fabs(derivative) < 1e-12)
        {
            printf("Derivative too close to zero.\n");
            return NAN;
        }

        double next = y - f(y) / derivative;

        if (fabs(next - y) < tolerance)
            return next;

        y = next;
    }

    return y;
}

int main(void)
{
    double tolerance = 1e-12;

    double root1 = newton_raphson(0.7, tolerance);
    double root2 = newton_raphson(-0.2, tolerance);

    printf("Root 1 = %.10f\n", root1);
    printf("Root 2 = %.10f\n", root2);

    printf("Residual at root 1 = %.3e\n", f(root1));
    printf("Residual at root 2 = %.3e\n", f(root2));

    return 0;
}

