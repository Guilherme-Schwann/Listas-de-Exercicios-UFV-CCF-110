#include <stdio.h>
#include <stdlib.h>

int divs(int x, int y) {
    if (x < 0)
        x *= -1;
    if (y < 0)
        y *= -1;
    if (y == 0)
        return -1;
    else if (x == y)
        return 1;
    else if (x < y)
        return 0;
    else
        return 1 + divs(x - y, y);
}
int main() {
    int x, y;
    scanf("%d %d", &x, &y);
    printf("%d\n", divs(x, y));
    system("PAUSE");
    return 0;
}