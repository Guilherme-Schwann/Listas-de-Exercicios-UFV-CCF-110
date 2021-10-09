#include <stdio.h>
#include <stdlib.h>

int primo(int);
int main() {
    int num, res;
    printf("Insira um número inteiro:");
    scanf("%d", &num);
    res = primo(num);
    if (res == 1) {
        printf("O numero %d eh primo.", num);
    } else {
        printf("O numero %d nao eh primo.", num);
    }
    system("PAUSE");
    return 0;
}
int primo(int num) {
    int resto, check;
    check = 1;
    for (int i = 2; i < num; i++){
        if (num % i == 0) {
            check = 0;
        }
    }
    return check;
}