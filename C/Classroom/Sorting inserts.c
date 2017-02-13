#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

//Сортировка вставками.

#define MAS_SIZE 10
int main()
{
	setlocale(LC_ALL, "rus");
	int mass[MAS_SIZE] = {8,9,7,0,6,5,2,3,1,4};
	int newElement,location;
	// Ввывод на экран до сортировки
	printf("До сортировки:\n");
	for (int s = 0; s < MAS_SIZE; s++)
	{
		printf("Число: %i\n",mass[s]);
	}
	printf("\n");
	//Сортировка
	for (int i = 1; i < MAS_SIZE; i++)
	{
		newElement = mass[i];
		location = i - 1;
		while (location >= 0 && mass[location] > newElement)
		{
			mass[location + 1] = mass[location];
			location = location - 1;
		}
		mass[location + 1] = newElement;
	}
	//Ввывод массива на экран после сортировки
	printf("После сортировки:\n");
	for (int h = 0; h < MAS_SIZE; h++)
	{
		printf("Число: %i\n",mass[h]);
	}
	getchar();
	printf("Good Jobs :)\n");
	return 0;
}

