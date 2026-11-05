#include <stdio.h>

#define NMAX 64

/* unit step: u[n] = 1 for n >= 0, else 0 */
int u(int n)
{
    return (n >= 0) ? 1 : 0;
}

/* AP as a causal sequence: x[k] = (a + (k-1) d) u[k-1] */
double ap(double a, double d, int k)
{
    return (a + (k - 1) * d) * u(k - 1);
}

/* S[n] = sum_k x[k] u[n-k]  (convolution of x with the unit step) */
double partial_sum(double a, double d, int n)
{
    double s = 0.0;

    for (int k = -NMAX; k <= NMAX; k++)
        s += ap(a, d, k) * u(n - k);

    return s;
}

int main(void)
{
    double d = 2.0;
    double nth_term = 4.0;
    double sum_n = -14.0;

    int n_found = -1;
    double a_found = 0.0;

    /* x[n] = 4 gives a = 4 - (n-1)d; search for n with S[n] = -14 */
    for (int n = 1; n <= 30; n++) {
        double a = nth_term - (n - 1) * d;

        if (partial_sum(a, d, n) == sum_n) {
            n_found = n;
            a_found = a;
        }
    }

    printf("Number of terms n = %d\n", n_found);
    printf("First term a = %.2f\n", a_found);
    printf("Sum of first 20 terms = %.2f\n", partial_sum(a_found, d, 20));

    return 0;
}
