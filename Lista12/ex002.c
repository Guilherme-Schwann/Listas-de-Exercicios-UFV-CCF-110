#include <stdio.h>
#include <stdlib.h>

int main() {

    double custofab, custo_ao_cons;
    int percdist, percimp;
    scanf("%lf", &custofab);
    percdist = 28; percimp = 45;
    custo_ao_cons = custofab + (custofab * percdist / 100);
    custo_ao_cons += custofab * percimp / 100;
    printf("Custo ao consumidor: R$%.2lf\n", custo_ao_cons);
    system("PAUSE");
    return 0;

}