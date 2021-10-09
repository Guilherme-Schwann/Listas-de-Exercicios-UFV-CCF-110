#include <stdio.h>
#include <stdlib.h>

int main() {
    int A[3][5], SL[3], soma;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 5; j++) {
            printf("Matriz[%d][%d]:", i, j);
            scanf("%d", &A[i][j]);
        }
    }
    for (int i = 0; i < 3; i++) {
        soma = 0;
        for (int j = 0; j < 5; j++) {
            soma += A[i][j];
        }
        SL[i] = soma;
        printf("Soma da linha %d: %d\n", i+1, SL[i]);
    }
    system("PAUSE");
    return 0;
}