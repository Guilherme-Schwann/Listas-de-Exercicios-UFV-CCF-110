#include <stdio.h>
#include <stdlib.h>

int soma(int *vetorPtr) {
    int result = 0, i;
    for (i = 0; i < 15; i++) {
        result += vetorPtr[i];
    }
    return result;
}

int main() {
    int vetor[15], res, i;
    int *vetorPtr = vetor;
    for (i = 0; i < 15; i++) {
        scanf("%d", &vetor[i]);
    }
    res = soma(vetorPtr);
    printf("%d\n", res);
    system("PAUSE");
    return 0;
}