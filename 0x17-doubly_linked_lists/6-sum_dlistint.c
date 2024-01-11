#include <stdlib.h>
#include "lists.h"

/**
 * sum_dlistint - sum nodes' val
 * @head: head of a doubly linked list
 * Return: sum of nodes' val
 */
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *tmp;
	int sum = 0;

	tmp = head;
	while (tmp)
	{
		sum += tmp->n;
		tmp = tmp->next;
	}

	return (sum);
}
