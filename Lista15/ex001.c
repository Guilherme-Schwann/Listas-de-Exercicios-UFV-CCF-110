#include <stdio.h>
#include <stdlib.h>

void quadrado(int lado, int total) {
    if (total == 0) {
        printf("\n");
        return;
    } else {
        if (total % (lado+1) == 0) {
            printf("\n");
            quadrado(lado, total - 1);
        } else {
            printf("* ");
            quadrado(lado, total - 1);
        }
    }
}

int main() {
    int d;
    scanf("%d", &d);
    quadrado(d, d*(d+1));
    system("PAUSE");
    return 0;
}