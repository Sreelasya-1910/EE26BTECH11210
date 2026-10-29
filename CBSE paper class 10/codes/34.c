#include <stdio.h>

int main(void) {
    double r1 = 0.10, r2 = 0.15;
    double interest = 1900.0;
    double extra = 200.0;

    // Equations:
    // r1*x + r2*y = interest
    // r2*x + r1*y = interest + extra

    double a = r1, b = r2;
    double c = r2, d = r1;
    double e = interest;
    double f = interest + extra;

    double determinant = a * d - b * c;

    double x = (e * d - b * f) / determinant;
    double y = (a * f - e * c) / determinant;

    printf("Amount lent at 10%% = Rs. %.2f\n", x);
    printf("Amount lent at 15%% = Rs. %.2f\n", y);

    return 0;
}

