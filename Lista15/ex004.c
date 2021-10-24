#include <stdio.h>
#include <stdlib.h>

void impar(int v1, int v2) {
    if (v1 == v2) {
        return;
    } else {
        if (v1 % 2 == 1)
            printf("%d\n", v1);
        impar(v1+1, v2);
    }
}

int main() {
    impar(0, 100);
    system("PAUSE");
    return 0;
}