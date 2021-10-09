#include <stdio.h>
#include <stdlib.h>

int FtoC(int temp) {
    int convTemp;
    convTemp = (temp - 32) / 1.8;
    return convTemp;
}

int FtoK(int temp) {
    int convTemp;
    convTemp = (temp - 32) * 5 / 9 + 273;
    return convTemp;
}

int CtoF(int temp) {
    int convTemp;
    convTemp = temp * 1.8 + 32;
    return convTemp;
}

int CtoK(int temp) {
    int convTemp;
    convTemp = temp + 273;
    return convTemp;
}

int KtoF(int temp) {
    int convTemp;
    convTemp = (temp - 273) * 1.8 + 32;
    return convTemp;
}

int KtoC(int temp) {
    int convTemp;
    convTemp = temp - 273;
    return convTemp;
}

int main() {
    int in, out, temp, convTemp;
    printf("Insira qual escala deseja converter e qual a escala desejada:\n");
    printf("Fahrenheit: 1\nCelsius: 2\nKelvin: 3\n");
    scanf("%d %d", &in, &out);
    printf("Insira a temperatura:");
    scanf("%d", &temp);
    switch (in) {
        case 1: switch (out) {
            case 2: convTemp = FtoC(temp); break;
            case 3: convTemp = FtoK(temp); break;
            } break;
        case 2: switch (out) {
            case 1: convTemp = CtoF(temp); break;
            case 3: convTemp = CtoK(temp); break;
            } break;
        case 3: switch (out) {
            case 1: convTemp = KtoF(temp); break;
            case 2: convTemp = KtoC(temp); break;
            } break;
    }
    printf("Temperatura convertida: %d\n", convTemp);
    system("PAUSE");
    return 0;
}