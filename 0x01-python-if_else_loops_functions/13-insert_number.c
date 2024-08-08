#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h;
	listint_t *temp;
	int key;

	h = malloc(sizeof(listint_t));
	if (h == NULL)
		return (NULL);

	h->n = number;
	h->next = NULL;

	key = number;

	if (*head == NULL || key < (*head)->n)
	{
		h->next = *head;
		*head = h;
	}

	else
	{
		temp = *head;
		while (temp->next != NULL && temp->next->n < key)
		{
			temp = temp->next;
		}
		h->next = temp->next;
		temp->next = h;
	}
	return (h);
}
