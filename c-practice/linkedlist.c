#include <stdio.h>

/*

*/
struct LinkedList {
  struct LinkedList *next;
  int data;
};

typedef struct LinkedList node;

void printlist(node *head) {
    while(head!=NULL) {
      printf("Head value is: %d \n", head->next);
      head = head->next;
    }
}

void add_node(node *head, node *next_node) {
  printf(head);
  printf(next_node);
  //head->next = next_node;
}

int main(void) {

  printf("%d", 1);
  node *n1;
  node *head;

  node n1obj;
  n1obj.data = 3;

  n1 = &n1obj;

  head->next = n1;

  //printf(head);
  //add_node(head, n1);
  //printlist(head);

}