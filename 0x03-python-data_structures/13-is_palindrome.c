#include "lists.h"

/**
 * is_palindrome - check if list is palindrome
 * @head: head of list
 * Return: 0 if list isn't palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	int *arr, len = 0;
	listint_t *h;

	h = *head;
	while (h != NULL)
	{
		len++;
		h = h->next;
	}

	if (len)
	{
		arr = list_to_array(*head, len);
		return (compare_and_free(arr, len));
	}
	return (1);
}

/**
 * list_to_array - convert list to array
 * @head: head of list
 * @len: length of list
 * Return: ptr to ints
 */
int *list_to_array(listint_t *head, int len)
{
	int i, *arr = malloc(sizeof(arr) * len);

	if (!arr)
		return (0);
	i = 0;
	while (head != NULL)
	{
		arr[i++] = head->n;
		head = head->next;
	}
	return (arr);
}

/**
 * compare_and_free - compare elts of array and free
 * @arr: ptr to list of array of int
 * @len: length of list
 * Return: 1 if list palindrome, 0 otherwise
 */
int compare_and_free(int *arr, int len)
{
	int i, j;

	if (!arr)
		return (0);
	for (i = 0, j = len - 1; i < len / 2; i++, j--)
	{
		if (arr[i] != arr[j])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
