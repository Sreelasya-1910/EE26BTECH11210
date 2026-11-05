#include <stdio.h>
/* Q3: Each of the 9 entries has 2 choices: sqrt(2) or sqrt(3). */
int main(void) {
    int entries = 3 * 3;
    int choices = 1;
    for (int i = 0; i < entries; ++i) choices *= 2;
    printf("Number of possible matrices = %d\n", choices); /* 512 */
    return 0;
}
