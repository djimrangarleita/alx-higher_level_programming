#include <stdlib.h>
#include "lists.h"

/**
 * insert_dnodeint_at_index - get node at pos index
 * @h: head of a doubly linked list
 * @idx: index where to insert the node
 * @n: data to insert in new node
 * Return: inserted node
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *tmp, *new_node;
	unsigned int i;

	if (idx == 0)
		return (add_dnodeint(h, n));

	i = 0;
	tmp = *h;
	while (tmp)
	{
		if (i + 1 == idx && !tmp->next)
			return (add_dnodeint_end(h, n));
		if (i + 1 == idx)
		{
			new_node = malloc(sizeof(dlistint_t));
			if (!new_node)
				return (NULL);

			new_node->n = n;
			new_node->next = tmp->next;
			new_node->prev = tmp;
			tmp->next = new_node;
			new_node->next->prev = new_node;

			return (new_node);
		}
		tmp = tmp->next;
		i++;
	}

	return (NULL);
}
