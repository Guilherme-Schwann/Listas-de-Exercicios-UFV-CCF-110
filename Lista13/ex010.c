#include <stdio.h>
#include <stdlib.h>

int menor(int *num) {
    int temp;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 2; j++) {
            if (num[j] > num[j+1]) {
                temp = num[j];
                num[j] = num[j+1];
                num[j+1] = temp;
            }
        }
    }
    return num[0];
}

int main() {
    int num[3];
    for (int i = 0; i < 3; i++) {
        scanf("%d", &num[i]);
    }
    printf("Menor: %d\n", menor(num));
    system("PAUSE");
    return 0;
}