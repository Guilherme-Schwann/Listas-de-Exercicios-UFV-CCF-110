#include <stdio.h>
#include <stdlib.h>

int main() {

    float sum;
    int i, div;
    for (i = 1; i <= 37; i++) {
        div = 38 - i;
        sum += (div * (div + 1)) / i;
    }
    printf("%f", sum);
    system("PAUSE");
    return 0;

}