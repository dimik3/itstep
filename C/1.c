#include <locale.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* Задание 1: В одномерном массиве, заполненном случайными числами, определить
минимальный и максимальный элементы.*/

#define SIZE 10
void randomNumber(int massiv[],int size);
void minMaxNumber(int massiv[],int size,int minN,int maxN);

int main()
{
	setlocale(LC_ALL, "rus");
	int massiv[SIZE];
	int minN = 0;
	int maxN = 0;
	randomNumber(massiv, SIZE);
	minMaxNumber(massiv, SIZE, minN, maxN);
	return 0;
}

void randomNumber(int massiv[],int size)
{
	srand(time(NULL));
	for (int i = 0; i < size; i++)
	{
		massiv[i] = rand() % 10;
		printf("Случайное число: %d\n", massiv[i]);
	}
}

void minMaxNumber(int massiv[],int size,int minN,int maxN)
{
	for (int j = 0; j<size; j++)
	{
		if (massiv[j] < massiv[minN])  // Если следущий элемент меньше минимального, то...
		{
			minN = j;
		} // назначаем его минимальным.
		if (massiv[j] > massiv[maxN])  // Если следущий элемент больше максимального, то...   
		{
			maxN = j;
		} // назначаем его максимальным.
	}
	printf("\nМинимальное число = %d.", massiv[minN]); // Выводим минимальный элемент.
	printf("\nМаксимальное число = %d.", massiv[maxN]); // Выводим максимальный элемент.
	getchar();
}