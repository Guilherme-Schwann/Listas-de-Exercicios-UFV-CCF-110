#include <stdio.h>
#include <stdlib.h>

void divPor3(int *vetorPtr) {
    for (int i = 0; i < 5; i++) {
        if (vetorPtr[i] % 3 == 0)
            printf("%d\n", vetorPtr[i]);
    }
}

int main() {
    int vetor[5], i;
    int *vetorPtr = vetor;
    for (i = 0; i < 5; i++) {
        scanf("%d", &vetor[i]);
    }
    divPor3(vetorPtr);
    system("PAUSE");
    return 0;
}