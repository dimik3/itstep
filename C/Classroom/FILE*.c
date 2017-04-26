#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <locale.h>

struct StockExchangeCourses
{
	float BuyDollar;
	float SellDollar;
	float BuyEuro;
	float SellEuro;
};

void writeСurrencyRate(struct StockExchangeCourses*  stockExchangeCourses, FILE* stockExchange)
{
	fwrite(stockExchangeCourses, sizeof(struct StockExchangeCourses), 1, stockExchange);
	/*printInfo(stockExchange);*/
}

void entreСurrencyRate()
{
	FILE* stockExchange = fopen("D:\\Sheblykin\\Блок ввода и вывода данных\\db.bin", "wb");
	struct StockExchangeCourses*  stockExchangeCourses = malloc(sizeof(struct StockExchangeCourses));
	printf("Please, entre Dollar rate (Buy): ");
	scanf("%f", &stockExchangeCourses->BuyDollar); 
	printf("Please, entre Dollar rate (Sell): ");
	scanf("%f", &stockExchangeCourses->SellDollar);
	printf("Please, entre Dollar rate (Buy): ");
	scanf("%f", &stockExchangeCourses->BuyEuro);
	printf("Please, entre Euro rate (Sell): ");
	scanf("%f", &stockExchangeCourses->SellEuro);
	writeСurrencyRate(stockExchangeCourses, stockExchange);


}


void printInfo(FILE* stockExchange)
{
	struct StockExchangeCourses* buff = malloc(sizeof(struct StockExchangeCourses));
	fread(buff, sizeof(struct StockExchangeCourses), 1, stockExchange);
	printf("BuyDollar: %.2f\n", buff->BuyDollar);
	printf("SellDollar: %.2f\n", buff->SellDollar);
	printf("BuyEuro: %.2f\n", buff->BuyEuro);
	printf("SellEuro: %.2f\n", buff->SellEuro);
}

int main()
{
	FILE* stockExchange = fopen("D:\\Sheblykin\\Блок ввода и вывода данных\\db.bin", "rb");
	if (stockExchange == NULL)
	{
		entreСurrencyRate();
	}
	else
	{
		printInfo(stockExchange);
	}
}
