#include <stdio.h>
#include "lists.h"

/**
 * print_dlistint - print doubly linked list
 * @h: head of a doubly linked list
 * Return: size of the list
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t listsize;

	if (!h)
		return (0);

	listsize = 0;
	while (h)
	{
		printf("%d\n", h->n);
		listsize++;
		h = h->next;
	}

	return (listsize);
}
