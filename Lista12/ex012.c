#include <stdio.h>
#include <stdlib.h>

int main(){
    int vetor1[10], vetor2[10];
    for (int i = 0; i < 10; i++) {
        printf("Item n %d:", i+1);
        scanf("%d", &vetor1[i]);
        vetor2[9-i] = vetor1[i];
    }
    for (int i = 0; i < 10; i++) {
        printf("Vetor 2, elemento %d: %d\n", i+1, vetor2[i]);
    }
    system("PAUSE");
    return 0;
}
