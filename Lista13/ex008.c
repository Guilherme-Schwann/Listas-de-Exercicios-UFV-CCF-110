#include <stdio.h>
#include <stdlib.h>

float convert(float meters) {
    float res;
    res = (meters * 39.37) / 12;
    return res;
}

int main() {
    float meters, converted;
    printf("Insira a medida em metros:");
    scanf("%f", &meters);
    converted = convert(meters);
    printf("A medida eh de %.2f pes e %.2f polegadas.\n", converted, converted * 12);
    system("PAUSE");
    return 0;
}