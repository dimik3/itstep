#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

/* Задание2: Пользователь вводит прибыль фирмы за год(12 месяцев). Затем пользователь
вводит диапазон(например, 3 и6 – поиск между3-м и6-м месяцем). Необходимо
определить месяц, в котором прибыль была максимальна и месяц, в котором прибыль
была минимальна с учетом выбранного диапазона. */

int main()
{
	setlocale(LC_ALL, "rus");
	const char Month[][10] = { "Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь" };
	int i, max = -1;
	int profit[12];
	int beg, end;
	for (i = 0; i<12; i++)
	{
		printf("Прибыль за %s: ", Month[i]); 
		scanf("%d", &profit[i]);
	}
	printf("Введите диапазон: ");
	scanf("%d %d", &beg, &end);
	if (beg<0 || beg >= 12 || end<0 || end >= 12)
		return -1;
	printf("С %s По %s: ", Month[beg], Month[end]);
	for (i = beg; i <= end; i++)
	{
		printf("%d ", profit[i]);
		if (max == -1 || profit[max]<profit[i])
			max = i;
	}
	printf("\nМаксимальная прибыль в %s: %d\n", Month[max], profit[max]);
	getchar();
	return 0;
}