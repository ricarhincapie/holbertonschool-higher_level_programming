#include "lists.h"

/**
* check_cycle - Checks whether or not there is a cycle
* @list: Header pointer to the list
* Return: 0 if no cycle, 1 if cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *head, *current;
	int n = 0;

	head = list;
	current = list;

	while (current->next != NULL && current->next != head)
		current = current->next;
	if (current->next == head)
		n = 1;
	return (n);
}
