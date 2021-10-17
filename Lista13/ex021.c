#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int somaQuad(int *vetorPtr) {
    int result = 0, i;
    for (i = 0; i < 20; i++) {
        result += pow(vetorPtr[i], 2);
    }
    return result;
}

int main() {
    int vetor[20], res, i;
    int *vetorPtr = vetor;
    for (i = 0; i < 20; i++) {
        scanf("%d", &vetor[i]);
    }
    res = somaQuad(vetorPtr);
    printf("%d\n", res);
    system("PAUSE");
    return 0;
}
