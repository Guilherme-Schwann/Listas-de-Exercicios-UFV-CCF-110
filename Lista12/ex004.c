#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main() {

    float num, res;
    scanf("%f", &num);
    if (num >=0)
        res = sqrt(num);
    else
        res = pow(num, 2);
    printf("%.2f", res);
    system("PAUSE");
    return 0;

}