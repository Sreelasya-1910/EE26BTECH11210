#include <stdio.h>

#define NMAX 64

/* unit step: u[n] = 1 for n >= 0, else 0 */
int u(int n)
{
    return (n >= 0) ? 1 : 0;
}

/* AP as a causal sequence starting at n = 0: x[n] = (a + n d) u[n] */
double ap(double a, double d, int n)
{
    return (a + n * d) * u(n);
}

/* y[n] = (x * u)[n] = sum_k x[k] u[n-k] = sum of x[0], ..., x[n] */
double running_sum(double a, double d, int n)
{
    double s = 0.0;

    for (int k = -NMAX; k <= NMAX; k++)
        s += ap(a, d, k) * u(n - k);

    return s;
}

int main(void)
{
    double d = 2.0;
    double last_term = 4.0;     /* x[m] = 4, the last term           */
    double sum_m = -14.0;       /* y[m] = -14, sum of x[0], ..., x[m] */

    int m_found = -1;
    double a_found = 0.0;

    /* x[m] = a + m d = 4 gives a = 4 - m d; search for m with y[m] = -14 */
    for (int m = 0; m <= 30; m++) {
        double a = last_term - m * d;

        if (running_sum(a, d, m) == sum_m) {
            m_found = m;
            a_found = a;
        }
    }

    printf("Last index m = %d, number of terms = %d\n", m_found, m_found + 1);
    printf("First term a = x[0] = %.2f\n", a_found);
    printf("Sum of first 20 terms = y[19] = %.2f\n", running_sum(a_found, d, 19));

    return 0;
}
