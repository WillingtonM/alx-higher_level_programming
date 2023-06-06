#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has cycle.
 * @list: pointer to the beginning of node
 * Return: if no cycle Return 0 otherwise return 1
 */
int check_cycle(listint_t *list)
{
  listint_t *current;
  listint_t *check;

  if (list == NULL || list->next == NULL) return (0);

  current = list;
  check = current->next;

  while (current != NULL && check->next != NULL
	 && check->next->next != NULL)
  {
    if (current == check)
      return (1);

    current = current->next;
    check = check->next->next;
  }
  
  return (0);
}
