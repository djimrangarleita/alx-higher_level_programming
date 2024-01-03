#include "lists.h"

/**
 * check_cycle - check if there a cycle in list
 * @list: ptr to listint_t to be checked
 * Return: 0 if no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;
	listptr_t *known_ptrs = NULL;

	tmp = list;
	while (tmp)
	{
		if (insert_ptr((void *)tmp, &known_ptrs))
		{
			free_tmp_list(known_ptrs);
			return (1);
		}
		tmp = tmp->next;
	}
	free_tmp_list(known_ptrs);

	return (0);
}

/**
 * insert_ptr - insert ptr to listptr if not exist
 * @newptr: ptr to be inserted into listptr_t
 * @head: head of listptr_t
 * Return: 0 on success, 1 otherwise
 */
int insert_ptr(void *newptr, listptr_t **head)
{
	listptr_t *new, *tmp;

	tmp = *head;
	while (tmp && tmp->next)
	{
		if ((void *)tmp->ptr == newptr)
			return (1);
		tmp = tmp->next;
	}

	new = malloc(sizeof(listptr_t));
	if (!new)
		return (1);
	new->ptr = newptr;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
		tmp->next = new;

	return (0);
}

/**
 * free_tmp_list - free list of known ptrs after execution
 * @head: head of the list of known ptrs
 */
void free_tmp_list(listptr_t *head)
{
	listptr_t *tmp;

	while (head != NULL)
	{
		tmp = head;
		head = (head)->next;
		free(tmp);
	}
}
