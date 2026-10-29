#include <stdio.h>

int main(void)
{
    /* Given measurements */
    double LM = 45.0;
    double MN = 63.0;
    double LN = 72.0;
    double AB = 5.0;

    /* Corresponding sides:
       LM <-> AB
       LN <-> AC
    */

    double scale = AB / LM;
    double AC = scale * LN;

    printf("Scale factor = %.6f\n", scale);
    printf("Length of AC = %.2f cm\n", AC);

    return 0;
}

