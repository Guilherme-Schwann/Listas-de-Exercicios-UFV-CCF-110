#include <stdio.h>
#include <stdlib.h>

void quadrado(int lado) {
    if (lado == 0 || lado %  == 0) {
        printf("\n");
    } else {
        printf("*");
        quadrado(lado-1);
    }
}

int main() {
    int d;
    scanf("%d", &d);
    quadrado(d*d);
    system("PAUSE");
    return 0;
}