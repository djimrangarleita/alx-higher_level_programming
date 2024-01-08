#include "lists.h"

/**
 * is_palindrome - checked if the l list of int is palindrome
 * @head: head of the list
 * Return: 0 if list isn't palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	int *arr, len = list_len(*head);

	if (len)
	{
		arr = list_to_array(*head, len);
		return (compare_and_free(arr, len));
	}
	return (1);
}

/**
 * list_len - caculate and return len of list
 * @h: ptr to the head of the list
 * Return: length of the list
 */
int list_len(listint_t *h)
{
	int count = 0;

	while (h != NULL)
	{
		count++;
		h = h->next;
	}
	return (count);
}

/**
 * list_to_array - convert a list to an array
 * @head: head of list
 * @len: length of the list
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
