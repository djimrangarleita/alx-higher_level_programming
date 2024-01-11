#include <stdio.h>
#include "lists.h"

/**
 * dlistint_len - calculate the length of dlist
 * @h: head of a doubly linked list
 * Return: size of the list
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t listsize;

	if (!h)
		return (0);

	listsize = 0;
	while (h)
	{
		listsize++;
		h = h->next;
	}

	return (listsize);
}
