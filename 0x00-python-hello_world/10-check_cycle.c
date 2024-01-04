#include "lists.h"

/**
 * check_cycle - check if there a cycle in list
 * @list: ptr to listint_t to be checked
 * Return: 0 if no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr;
	listint_t *fast_ptr;

	slow_ptr = list;
	fast_ptr = list;
	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
		if (slow_ptr == fast_ptr)
		{
			return (1);
		}
	}

	return (0);
}
