    
#include <stdio.h>
#include <math.h>

double f(double x)
{
    return x * x - 2.0 * x - 1.0;
}

double df(double x)
{
    return 2.0 * x - 2.0;
}

double newton_raphson(double x)
{
    const double tolerance = 1e-12;

    for (int i = 0; i < 100; i++)
    {
        double derivative = df(x);

        if (fabs(derivative) < 1e-14)
        {
            printf("Derivative too small.\n");
            return NAN;
        }

        double next = x - f(x) / derivative;

        if (fabs(next - x) < tolerance)
            return next;

        x = next;
    }

    return x;
}

int main(void)
{
    /* Initial guesses for the two zeroes */
    double alpha = newton_raphson(2.5);
    double beta  = newton_raphson(-0.5);

    printf("Alpha = %.10f\n", alpha);
    printf("Beta  = %.10f\n", beta);

    double result = 1.0 / (2.0 * alpha)
                  + 1.0 / (2.0 * beta)
                  + 3.0 * alpha * beta;

    printf("Required value = %.10f\n", result);

    return 0;
}
   
