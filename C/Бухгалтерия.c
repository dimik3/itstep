#include <stdio.h>
#include <locale.h>
/*
Написать программу, которая дает пользователю вести домашнюю бухгалтерию. В начале
программа спрашивает текущий баланс счета. Затем программа выводит меню:
1.  Снять со счета
2.  Положить на счет
3.  Вывести на экран список транзакций
4.  Вывести баланс
5.  Выход
Сумма вводится как вещественное число(BYN). К каждой транзакции можно писать
комментарий с указанием типа/содержания транзакции.
*/

enum Menu
{
	snyatSoScheta = 1,
	polojitbNaSchet,
	printListTranzakciy,
	printBalance
}menu;

struct Accounting
{
	float score;
	float balanceAdd;
	float balanceDel;
	int tAdd;
	int tDel;

}myStruct;

void enterBalance(float* score)
{
	printf("Текущий баланс счета: ");
	scanf("%f",score);
}

void printMenu()
{
	printf("1.Снять со счета\n");
	printf("2.Положить на счет\n");
	printf("3.Вывести на экран список транзакций\n");
	printf("4.Вывести баланс\n");
	printf("5.Выход\n");
	scanf("%i", &menu);
}

void enterValue(float* score,float* balanceAdd,float* balanceDel,int* tAdd,int* tDel)
{
	while (menu != 0)
	{
		switch (menu)
		{
		case snyatSoScheta:
			printf("\nСколько хотите снять денег со счета ?: ");
			scanf("%f", balanceDel);
			*score -= *balanceDel;
			*tDel += 1;
			printf("Успешно.\n");
			break;
		case polojitbNaSchet:
			printf("\nСколько хотите положить денег на счет ?: ");
			scanf("%f", balanceAdd);
			*score += *balanceAdd;
			*tAdd += 1;
			printf("Ваш баланс успешно пополнен.\n");
			break;
		case printListTranzakciy:
			printf("\n\t\t\t     СПИСОК ОПЕРАЦИЙ:\n\tПополнение баланса: %i раз(а)\tСнятия средств с баланса: %i раз(а)\n",*tAdd,*tDel);
			break;
		case printBalance:
			printf("\nВаш баланс состовляет: %f\n", *score);
			break;
		}
		if (menu >= 5)
		{
			break;
		}
		printf("\n");
		printMenu();
	}
}

int main()
{
	setlocale(LC_ALL, "rus");
	myStruct.score = 0.0;
	myStruct.balanceAdd = 0.0;
	myStruct.balanceDel = 0.0;
	myStruct.tAdd = 0;
	myStruct.tDel = 0;
	enterBalance(&myStruct.score);
	printMenu();
	enterValue(&myStruct.score,&myStruct.balanceAdd,&myStruct.balanceDel,&myStruct.tAdd,&myStruct.tDel);
}