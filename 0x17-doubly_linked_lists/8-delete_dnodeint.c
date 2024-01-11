#include <stdlib.h>
#include "lists.h"

/**
 * delete_dnodeint_at_index - get node at pos index
 * @head: head of a doubly linked list
 * @index: index where to insert the node
 * Return: insert 1 on success, -1 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *tmp;
	unsigned int i;

	if (index == 0)
		return (delete_dnodeint_head(head));

	i = 0;
	tmp = *head;
	while (tmp)
	{
		if (i + 1 == index && !tmp->next->next)
		{
			free(tmp->next);
			tmp->next = NULL;

			return (1);
		}
		if (i + 1 == index && tmp->next)
		{
			tmp->next = tmp->next->next;
			free(tmp->next->prev);
			tmp->next->prev = tmp;

			return (1);
		}
		tmp = tmp->next;
		i++;
	}

	return (-1);
}

/**
 * delete_dnodeint_head - delete head node
 * @head: ptr to head of list
 * Return: 1 on success
 */
int delete_dnodeint_head(dlistint_t **head)
{
	dlistint_t *tmp;

	tmp = *head;
	if (tmp)
	{
		*head = tmp->next;
		if (tmp->next)
			tmp->next->prev = NULL;
		free(tmp);

		return (1);
	}
	return (-1);
}
