#include <stdio.h>

#define N 6

/* Map each outcome to 1 if it is not a factor of 36,
   otherwise map it to 0. */
int event_map(int outcome)
{
    return (36 % outcome != 0) ? 1 : 0;
}

int main(void)
{
    int mapping[N];
    int count = 0;

    /* Step 1: Map outcomes to binary values */
    printf("Outcome: ");
    for (int i = 1; i <= N; i++)
        printf("%d ", i);

    printf("\nMapping: ");
    for (int i = 1; i <= N; i++)
    {
        mapping[i - 1] = event_map(i);
        printf("%d ", mapping[i - 1]);
        count += mapping[i - 1];
    }

    /* Step 2: Assign equal probabilities */
    double probability = 0.0;

    for (int i = 0; i < N; i++)
        probability += mapping[i] * (1.0 / N);

    printf("\n\nFavourable outcomes = %d\n", count);
    printf("Probability = %.6f\n", probability);
    printf("Exact probability = %d/%d\n", count, N);

    return 0;
}

