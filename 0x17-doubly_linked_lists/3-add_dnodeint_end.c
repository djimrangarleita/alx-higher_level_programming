#include <stdlib.h>
#include "lists.h"

/**
 * add_dnodeint_end - add new node to end
 * @head: head of a doubly linked list
 * @n: int data to add to the node
 * Return: head of list
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new_node;
	dlistint_t *tmp;

	new_node = malloc(sizeof(dlistint_t));
	if (!new_node)
		return (NULL);

	new_node->n = n;
	new_node->next = NULL;

	tmp = *head;
	if (tmp)
	{
		while (tmp->next)
			tmp = tmp->next;

		tmp->next = new_node;
	}
	new_node->prev = tmp;

	if (!tmp)
		*head = new_node;

	return (new_node);
}
