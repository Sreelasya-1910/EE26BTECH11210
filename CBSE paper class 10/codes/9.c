
#include <stdio.h>

int gcd(int a, int b)
{
    while (b != 0)
    {
        int remainder = a % b;
        a = b;
        b = remainder;
    }

    return a;
}

int lcm(int a, int b)
{
    return (a / gcd(a, b)) * b;
}

int main(void)
{
    int x = lcm(lcm(4, 6), 8);
    int y = lcm(lcm(3, 5), 7);
    int p = lcm(x, y);

    printf("x = %d\n", x);
    printf("y = %d\n", y);
    printf("p = %d\n", p);

    if (p == 35 * x)
        printf("Correct option: A (p = 35x)\n");

    return 0;
}

