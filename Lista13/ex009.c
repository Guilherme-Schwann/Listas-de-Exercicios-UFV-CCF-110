#include <stdio.h>
#include <stdlib.h>

int posOrNeg(int num) {
    if (num < 0)
        return 0;
    else
        return 1;
}

int main() {
    int n, res;
    scanf("%d", &n);
    res = posOrNeg(n);
    if (res == 0)
        printf("O numero %d eh negativo.\n", n);
    else
        printf("O numero %d eh positivo.\n", n);
    system("PAUSE");
    return 0;
}