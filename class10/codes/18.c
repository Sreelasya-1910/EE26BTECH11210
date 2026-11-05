#include <stdio.h>

int main(void)
{
    /*
       Given:
       Triangle DEF and triangle PQR
       angle D = angle Q
       angle E = angle R

       Therefore, by AA similarity:
       D <-> Q
       E <-> R
       F <-> P

       Corresponding sides:
       DE <-> QR
       EF <-> RP
       DF <-> PQ
    */

    double DE = 6.0, QR = 3.0;
    double EF = 8.0, RP = 4.0;
    double DF = 10.0, PQ = 5.0;

    printf("Option A: DE/QR = %.2f, DF/PQ = %.2f\n",
           DE / QR, DF / PQ);

    printf("Option B: EF/RP = %.2f, DF/PQ = %.2f\n",
           EF / RP, DF / PQ);

    printf("Option C: EF/RP = %.2f, DE/QR = %.2f\n",
           EF / RP, DE / QR);

    printf("Option D: DE/PQ = %.2f, EF/RP = %.2f\n",
           DE / PQ, EF / RP);

    return 0;
}

