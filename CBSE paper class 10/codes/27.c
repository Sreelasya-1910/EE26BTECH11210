
#include <stdio.h>

#define N 3

int main(void)
{
    /* Order: Black, Brown, Blue */
    double p[N] = {0.65, 0.25, 0.10};

    /* Event (a): Blue eyes */
    int map_blue[N] = {0, 0, 1};

    /* Event (b): Brown or black eyes */
    int map_brown_black[N] = {1, 1, 0};

    double P_blue = 0.0;
    double P_brown_black = 0.0;

    printf("Eye colours: Black Brown Blue\n");

    printf("Mapping (a): ");
    for (int i = 0; i < N; i++)
    {
        printf("%d ", map_blue[i]);
        P_blue += p[i] * map_blue[i];
    }

    printf("\nMapping (b): ");
    for (int i = 0; i < N; i++)
    {
        printf("%d ", map_brown_black[i]);
        P_brown_black += p[i] * map_brown_black[i];
    }

    printf("\n\nP(Blue eyes) = %.2f\n", P_blue);
    printf("P(Brown or Black eyes) = %.2f\n", P_brown_black);

    return 0;
}

