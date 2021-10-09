#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, sum;
    sum = 0;
    printf("Tamanho do vetor:");
    scanf("%d", &n);
    int vetor[n];
    for (int i = 0; i < n; i++) {
        printf("Item n %d:", i);
        scanf("%d", &vetor[i]);
        if (i % 2 == 0) {
            sum += vetor[i];
        }
    }
    printf("Soma dos itens de index par: %d\n", sum);
    system("PAUSE");
    return 0;
}