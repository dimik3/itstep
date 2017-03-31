#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
Задание 1:
Написать программу, которая дает пользователю ввести 5 фамилий студентов и хранит их
в динамическом массиве, а затем сортирует их по возрастанию
*/

#define COUNT 5

void Array(char** list)
{

	for (int i = 0; i < COUNT; i++)
	{
		*(list + i) = malloc(50 * sizeof(char));
		printf("Enter last name %i: ", i + 1);
		fgets(list[i], 200, stdin);
	}
}

void sortBubble(char** list)
{
	for (int i = 0; i < COUNT; i++)
	{
		for (int j = 0; j < COUNT - i - 1; j++)
		{
			if (strcmp(list[j], list[j + 1]) > 0)
			{
				char* temp = list[j];
				list[j] = list[j + 1];
				list[j + 1] = temp;
			}
		}

	}
}

void printArray(char** list)
{
	for (int i = 0; i < COUNT; i++)
	{
		printf("\nLast name %i: %s", i + 1, list[i]);
		printf("\n");
	}
}

void deleteListArray(char** list)
{
	printf("\nStart clear memory...\n");
	for (int i = 0; i < COUNT; i++)
	{
		free(list[i]);
	}
	free(list);
	printf("\nReady :)\n");
}

int main()
{
	char** list = malloc(COUNT * sizeof(char*));;
	Array(list);
	sortBubble(list);
	printArray(list);
	deleteListArray(list);
}