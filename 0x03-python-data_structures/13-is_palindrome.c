#include <stddef.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: double pointer  to the first node
 * Return: 1 if list is a palindrome, otherwise return 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int vals[2048];
	int c_loop; 
	int lmt;
	int i = 0;

	if (head == NULL || *head == NULL)
		return (1);

	while (tmp != NULL)
	{
		vals[i] = tmp->n;
		i++;
		tmp = tmp->next;
	}

	lmt = (i % 2 == 0) ? i / 2 : (i + 1) / 2;

	for (c_loop = 0; c_loop < lmt; c_loop++)
		if (vals[c_loop] != vals[i - 1 - c_loop])
			return (0);

	return (1);
}
