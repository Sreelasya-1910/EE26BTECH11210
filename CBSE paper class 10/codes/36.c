#include <stdio.h>

#define N 6

typedef struct {
    int lower;
    int upper;
    int frequency;
} RainfallClass;

int totalSubdivisions(const RainfallClass data[]) {
    int total = 0;

    for (int i = 0; i < N; i++)
        total += data[i].frequency;

    return total;
}

int modalClass(const RainfallClass data[]) {
    int index = 0;

    for (int i = 1; i < N; i++) {
        if (data[i].frequency > data[index].frequency)
            index = i;
    }

    return index;
}

double meanRainfall(const RainfallClass data[]) {
    double weightedSum = 0.0;
    int total = totalSubdivisions(data);

    for (int i = 0; i < N; i++) {
        double midpoint =
            (data[i].lower + data[i].upper) / 2.0;

        weightedSum += midpoint * data[i].frequency;
    }

    return weightedSum / total;
}

double medianRainfall(const RainfallClass data[]) {
    int total = totalSubdivisions(data);
    double half = total / 2.0;
    int cumulative = 0;

    for (int i = 0; i < N; i++) {
        int previousCF = cumulative;
        cumulative += data[i].frequency;

        if (cumulative >= half) {
            double l = data[i].lower;
            double h = data[i].upper - data[i].lower;
            double f = data[i].frequency;

            return l + ((half - previousCF) / f) * h;
        }
    }

    return -1.0;
}

int goodRainfallCount(const RainfallClass data[]) {
    int count = 0;

    for (int i = 0; i < N; i++) {
        if (data[i].lower >= 800)
            count += data[i].frequency;
    }

    return count;
}

int main(void) {
    RainfallClass data[N] = {
        {200,  400, 3},
        {400,  600, 4},
        {600,  800, 7},
        {800, 1000, 4},
        {1000, 1200, 3},
        {1200, 1400, 3}
    };

    int mode = modalClass(data);

    printf("Total subdivisions: %d\n",
           totalSubdivisions(data));

    printf("Modal class: %d-%d mm\n",
           data[mode].lower, data[mode].upper);

    printf("Median rainfall: %.2f mm\n",
           medianRainfall(data));

    printf("Mean rainfall: %.2f mm\n",
           meanRainfall(data));

    printf("Subdivisions with good rainfall: %d\n",
           goodRainfallCount(data));

    return 0;
}

