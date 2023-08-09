#include "lists.h"

/**
 * check_cycle - checks for a cycle in a linked list
 * @list: pointer to the list
 * Return: 0 if no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *faster, *slow;

	slow = list;
	faster = list;

	while (faster != NULL)
	{
		slow = slow->next;
		faster = faster->next->next;
		if (faster == slow)
			return (1);
	}
	return (0);
}
