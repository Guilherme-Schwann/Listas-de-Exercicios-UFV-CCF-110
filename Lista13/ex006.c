#include <stdio.h>
#include <stdlib.h>

float average(float n1, float n2, float n3) {
    float media;
    media = (n1 + n2 + n3) / 3;
    return media;
}
int main() {
    float n1, n2, n3, media;
    printf("Insira as notas:");
    scanf("%f %f %f", &n1, &n2, &n3);
    media = average(n1, n2, n3);
    printf("Media: %.1f\n", media);
    system("PAUSE");
    return 0;
}