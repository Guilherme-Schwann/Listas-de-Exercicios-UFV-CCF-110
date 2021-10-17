#include <stdio.h>
#include <stdlib.h>

void crescente(int *vetorPtr) {
    int temp;
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 9; j++) {
            if (vetorPtr[j] > vetorPtr[j+1]) {
                temp = vetorPtr[j];
                vetorPtr[j] = vetorPtr[j+1];
                vetorPtr[j+1] = temp;
            }
        }
    }
}

int main() {
    int vetor[10], i;
    int *vetorPtr = vetor;
    for (i = 0; i < 10; i++) {
        scanf("%d", &vetor[i]);
    }
    crescente(vetorPtr);
    for (i = 0; i < 10; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");
    system("PAUSE");
    return 0;
}