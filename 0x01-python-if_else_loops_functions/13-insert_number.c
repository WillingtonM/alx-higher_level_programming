#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: Pointer to head of linked list.
 * @number: Number to insert.
 * Return: If function fails Return 0 or pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new; 
	listint_t *node = *head;

	new = malloc(sizeof(listint_t));
	
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;

		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
