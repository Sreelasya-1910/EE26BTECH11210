#include <stdio.h>
#include <math.h>

int main(void)
{
    double d = 2.0;
    double nth_term = 4.0;
    double sum_n = -14.0;

    /*
       From the nth-term and sum formulas:
       n^2 - 5n - 14 = 0
    */

    double A = 1.0;
    double B = -5.0;
    double C = -14.0;

    double discriminant = B * B - 4.0 * A * C;

    double n1 = (-B + sqrt(discriminant)) / (2.0 * A);
    double n2 = (-B - sqrt(discriminant)) / (2.0 * A);

    double n = (n1 > 0.0) ? n1 : n2;

    /* Calculate the first term */
    double a = nth_term - (n - 1.0) * d;

    /* Sum of the first 20 terms */
    int N = 20;
    double S20 = (N / 2.0) * (2.0 * a + (N - 1) * d);

    printf("Number of terms n = %.0f\n", n);
    printf("First term a = %.2f\n", a);
    printf("Sum of first 20 terms = %.2f\n", S20);

    return 0;
}

