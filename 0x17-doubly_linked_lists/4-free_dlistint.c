#include <stdlib.h>
#include "lists.h"

/**
 * free_dlistint - free list
 * @head: head of a doubly linked list
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *tmp;

	tmp = head;
	while (tmp)
	{
		head = tmp->next;
		free(tmp);
		tmp = head;
	}
}
