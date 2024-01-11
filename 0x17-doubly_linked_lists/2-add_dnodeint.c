#include <stdlib.h>
#include "lists.h"

/**
 * add_dnodeint - add new node to head
 * @head: head of a doubly linked list
 * @n: int data to add to the node
 * Return: head of list
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new_node;
	dlistint_t *tmp;

	new_node = malloc(sizeof(dlistint_t));
	if (!new_node)
		return (NULL);

	tmp = *head;

	new_node->n = n;
	new_node->prev = NULL;
	new_node->next = tmp;

	if (tmp)
		tmp->prev = new_node;
	*head = new_node;

	return (new_node);
}
