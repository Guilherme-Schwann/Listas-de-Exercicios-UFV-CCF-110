#include <stdio.h>
#include <stdlib.h>

void tabuada(int ntab, int n) {
    if (ntab < 0) {
        return;
    } else {
        printf("%d\n", (n-ntab)*n);
        tabuada(ntab-1, n);
    }
}

int main() {
    int n;
    scanf("%d", &n);
    tabuada(n-1, n);
    system("PAUSE");
    return 0;
}