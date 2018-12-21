#include <stdio.h>

int main(void) {
    /*int a = 5;
    int *p = &a;
    int **b;
    **b = 3;
    printf("value of p is: %d\n", *p);
    printf("value of string is: %s", );*/
    int a = 5;
    printf("Value a is : %d\n", a);
    printf("Address a is : %p\n", &a);
    int *p;
    p = &a;
    printf("Value *p is : %d\n", *p);
    printf("address p is : %p\n", &p);
    printf("address p is : %p\n", p+1);
    printf("address p is : %p\n", p+2);
}
