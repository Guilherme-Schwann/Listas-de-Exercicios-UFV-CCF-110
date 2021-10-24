#include <stdio.h>
#include <stdlib.h>

int mod(int x, int y) {
    if (x < 0)
        x *= -1;
    if (y < 0)
        y *= -1;
    if (y == 0)
        return -1;
    else if (x == y)
        return 0;
    else if (x < y)
        return x;
    else
        return mod(x - y, y);
}
int main() {
    int x, y;
    scanf("%d %d", &x, &y);
    printf("%d\n", mod(x, y));
    system("PAUSE");
    return 0;
}