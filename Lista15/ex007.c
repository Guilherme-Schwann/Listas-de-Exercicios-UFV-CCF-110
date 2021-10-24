#include <stdio.h>
#include <stdlib.h>

int fibo(int termo) {
    if (termo == 1 || termo == 2)
        return 1;
    else
        return fibo(termo - 1) + fibo(termo - 2);
}
int main() {
    int ordem = 20;
    for (int i = 1; i <= ordem; i++)
        printf("%d ", fibo(i));
    printf("\n");
    system("PAUSE");
    return 0;
}