#include <stdio.h>

int main(void) {
  char *a = "abc\0\0";

  char s1[10] = {'a', 'b', 'c', '\0'};

  printf(a);
  printf(sizeof(s1));
}