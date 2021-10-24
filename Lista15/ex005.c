#include <stdio.h>
#include <stdlib.h>

int mdc(int x, int y) {
    if (x > y)
        mdc(x-y, y);
    else if (y > x)
        mdc(y, x);
    else
        return x;
}
int main() {
    int x, y, res;
    scanf("%d %d", &x, &y);
    res = mdc(x, y);
    printf("%d\n", res);
    system("PAUSE");
    return 0;
}