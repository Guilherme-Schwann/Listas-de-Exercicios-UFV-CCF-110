#include <stdio.h>
#include <stdlib.h>

int fat(int x) {
    if (x == 0)
        return 1;
    else
        return x * fat(x-1);
}
int main() {
    int x;
    scanf("%d", &x);
    printf("%d\n", fat(x));
    system("PAUSE");
    return 0;
}