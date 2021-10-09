#include <stdio.h>
#include <stdlib.h>

int reverse(int n) {
    int revn, c, d, u;
    c = n / 100;
    d = (n - c * 100) / 10;
    u = n % 10;
    revn = (u * 100) + (d * 10) + c;
    return revn;
}

int main() {
    int num, revnum;
    scanf("%d", &num);
    revnum = reverse(num);
    printf("Revertendo: %d\n", revnum);
    system("PAUSE");
    return 0;
}