#include "lists.h"

/**
 * print_list - print string and its length
 * @h: head of list
 * Return: length of string
 */
size_t print_list(const list_t *h)
{
	size_t nodes = 0;
	int len;

	while (h)
	{
		len = strlen(h->str);
		if (len != 0)
			printf("[%d] %s\n", len, h->str);
		else
			printf("[%d] %s\n", len, "(nil)");
		h = h->next;
		nodes++;
	}
	return (nodes);
}
