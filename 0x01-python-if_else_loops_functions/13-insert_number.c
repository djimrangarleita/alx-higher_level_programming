#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert new node in a sorted list
 * @head: head of sorted list
 * @number: number to be inserted
 * Return: address of new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *tmp;

	tmp = *head;
	if (!tmp || (!tmp->next && tmp->n < number))
	{
		return (add_nodeint_end(head, number));
	}
	else if (!tmp->next && tmp->n > number)
	{
		return (add_nodeint_head(head, number));
	}

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;

	while (tmp)
	{
		if (!tmp->next)
		{
			tmp->next = newnode;
			break;
		}
		else if ((tmp->n < number && tmp->next->n > number) ||
				(tmp->n > number && tmp->next->n < number))
		{
			newnode->next = tmp->next;
			tmp->next = newnode;
			break;
		}
		tmp = tmp->next;
	}
	return (newnode);
}

/**
 * add_nodeint_head - insert a new node in the head pos of the list
 * @head: ptr to head of list
 * @n: int number to insert to head
 * Return: new node ptr
 */
listint_t *add_nodeint_head(listint_t **head, const int n)
{
	listint_t *newnode;

	newnode = malloc(sizeof(listint_t));

	if (!newnode)
		return (NULL);

	newnode->n = n;
	newnode->next = *head;

	*head = newnode;

	return (newnode);
}
