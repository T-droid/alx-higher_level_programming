#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the address to the head pointer
 * Return: 0 if not a palindrome or 1 if otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *rev, **cp_head;
	int mid = 0, count = 0;

	cp_head = head;
	rev = reverse_listint(cp_head, &count);

	ptr = *head;

	while (mid == count / 2)
	{
		if (ptr->n != rev->n)
			return (0);
		mid++;
		ptr = ptr->next;
		rev = rev->next;
	}
	return (1);
}


/**
 * reverse_listint - reverses a linked list
 * @count: counts the number of nodes
 * @head: address to head pointer
 * Return: pointer to the reversed list
 */
listint_t *reverse_listint(listint_t **head, int *count)
{
	listint_t *ptr = NULL, *temp;

	if (*head == NULL)
		return (NULL);
	if ((*head)->next == NULL)
		return (*head);

	temp = (*head)->next;
	while (*head != NULL)
	{
		(*head)->next = ptr;
		ptr = *head;
		*head = temp;
		if (temp != NULL)
			temp = temp->next;
		*count += 1;
	}
	*head = ptr;
	return (*head);
}
