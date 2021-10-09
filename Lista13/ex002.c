#include <stdio.h>
#include <stdlib.h>

int imparPar(int);
int main() {
    int num, res;
    printf("Insira um número inteiro:");
    scanf("%d", &num);
    res = imparPar(num);
    if (res == 0)
        printf("O número %d é par.\n", num);
    else if (res == 1)
        printf("O número %d é ímpar.\n", num);
    system("PAUSE");
    return 0;
}
int imparPar(int num) {
    int res;
    res = num % 2;
    return res;
}