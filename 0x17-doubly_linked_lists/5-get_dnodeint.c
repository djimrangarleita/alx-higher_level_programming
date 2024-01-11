#include <stdlib.h>
#include "lists.h"

/**
 * get_dnodeint_at_index - get node at pos index
 * @head: head of a doubly linked list
 * @index: index of the node to get and return
 * Return: node at pos index
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *tmp;
	unsigned int i;

	if (index == 0)
		return (head);

	i = 0;
	tmp = head;
	while (tmp)
	{
		if (i + 1 == index)
			return (tmp->next);
		tmp = tmp->next;
		i++;
	}

	return (NULL);
}
