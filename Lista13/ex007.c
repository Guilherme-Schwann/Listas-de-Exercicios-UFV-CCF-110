#include <stdio.h>
#include <stdlib.h>

int aprRepr(float * notas) {
    int res, media = 0;
    for (int i = 0; i < 5; i++) {
        media += notas[i];
    }
    if (media / 5 >= 60)
        res = 1;
    else
        res = 0;
    return res;
}

int main() {
    float notas[10][5];
    int res;
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 5; j++) {
            printf("Aluno %d, nota %d:", i+1, j+1);
            scanf("%f", &notas[i][j]);
        }
        res = aprRepr(notas[i]);
        if (res == 1)
            printf("Aluno %d aprovado!\n", i+1);
        else
            printf("Aluno %d reprovado!\n", i+1);
    }
    system("PAUSE");
    return 0;
}