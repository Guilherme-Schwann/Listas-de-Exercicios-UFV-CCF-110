#include <stdio.h>
#include <stdlib.h>

void mulDe5(int v1, int v2) {
    if (v1 == v2-1) {
        return;
    } else {
        if ((v1+1) % 5 == 0)
            printf("%d\n", v1+1);
        mulDe5(v1+1, v2);
    }
}

int main() {
    int v1, v2;
    scanf("%d %d", &v1, &v2);
    mulDe5(v1,v2);
    system("PAUSE");
    return 0;
}