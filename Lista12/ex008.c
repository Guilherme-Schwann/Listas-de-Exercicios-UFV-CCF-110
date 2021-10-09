#include <stdio.h>
#include <stdlib.h>

int main() {
    int soma, num;
    num = 0; soma = 0;
    while (num >= 0) {
        soma += num;
        scanf("%d", &num);
    }
    printf("Soma = %d\n", soma);
    system("PAUSE");
    return 0;
}