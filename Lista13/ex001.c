#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float deltaf(float, float, float);
float raiz1f(float, float, float);
float raiz2f(float, float, float);
int main() {
    float a, b, c, delta, raiz1, raiz2;
    printf("Insira os termos A, B e C da equação:");
    scanf("%f %f %f", &a, &b, &c);
    delta = deltaf(a, b, c);
    raiz1 = raiz1f(a, b, delta);
    raiz2 = raiz2f(a, b, delta);
    printf("O delta da equação é %.2f\n", delta);
    printf("As raízes da equação são %.2f e %.2f\n", raiz1, raiz2);
    system("PAUSE");
    return 0;
}

float deltaf(float a, float b, float c) {
    float res;
    res = pow(b, 2);
    res -= 4 * a * c;
    return res;
}

float raiz1f(float a, float b, float delta) {
    float raiz1, com;
    com = (-1) * b;
    raiz1 = (com + sqrt(delta))/(2 * a);
    return raiz1;
}
float raiz2f(float a, float b, float delta) {
    float raiz2, com;
    com = (-1) * b;
    raiz2 = (com - sqrt(delta))/(2 * a);
    return raiz2;
}