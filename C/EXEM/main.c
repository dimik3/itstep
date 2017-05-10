#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <locale.h>
#include <direct.h>
#include <windows.h>

/*
Разработать программу хранения рецептов.
При запуске программа показывает меню.
Меню:
1. Добавление рецепта
2. Просмотр рецепта
3. Редактирование рецепта
4. Удаление рецепта
5. Выход
Каждый рецепт должен содержать следующую информацию:
1. Дату создания рецепта
2. Имя рецепта
3. Текст рецепта
4. Рейтинг (от 1 до 10)
*/


struct Recipe
{
	char name[50];
	char date[30];
	char text[1024];
	char rating[10];
};


enum Menu
{
	AddRecipe = '1',
	ShowAllRecipe = '2',
	VieRecipe = '3',
	EditRecipe = '4',
	DelReciep = '5',
	Exit = '0',
};

void recipeInfo(struct Recipe* recipeAdd, struct Recipe* buff,
	char* fileName, char* Bonding, char* dir);
void addRecipe(struct Recipe* recipeAdd,
	char* fileName, char* Bonding, char* dir);
void viewRecipe(struct Recipe* buff,
	char* fileName, char* Bonding, char* dir);
void editRecipe(struct Recipe* buff,
	char* fileName, char* Bonding, char* dir);
void delReciep(char* fileName, char* Bonding, char* dir);
void showAllRecipe(char* Bonding);


int main()
{
	setlocale(LC_ALL, "rus");
	struct Recipe* recipeAdd = malloc(sizeof(struct Recipe));
	struct Recipe* buff = malloc(sizeof(struct Recipe));
	char* fileName = (char *)malloc(200);;
	char* Bonding = (char *)malloc(200);
	char* dir = (char *)malloc(200);
	printf("\t\t =*=*=*=*=*=*= Книга рецептов =*=*=*=*=*=*= \n\n");
	recipeInfo(recipeAdd, buff, fileName, Bonding, dir);
	return 0;
}

void recipeInfo(struct Recipe* recipeAdd, struct Recipe* buff,
	char* fileName, char* Bonding, char* dir)
{
	while (true)
	{
		printf("Выберите пункт меню:\n");
		printf("1 - Добавление рецепта\n2 - Показать все рецепты на диске\n3 - Просмотр рецепта\n4 - Редактирование рецепта\n5 - Удаление рецепта\n0 - Выход\n");
		char pressKey = getch();
		switch (pressKey)
		{
		case AddRecipe:
			system("cls");
			addRecipe(recipeAdd, fileName, Bonding, dir);
			break;
		case VieRecipe:
			system("cls");
			viewRecipe(buff, fileName, Bonding, dir);
			break;
		case EditRecipe:
			system("cls");
			editRecipe(buff, fileName, Bonding, dir);
			break;
		case DelReciep:
			system("cls");
			delReciep(fileName, Bonding, dir);
			break;
		case ShowAllRecipe:
			system("cls");
			showAllRecipe(Bonding);
			printf("\n");
			continue;
		case Exit:
			return 0;
			break;
		default:
			system("cls");
			printf("\nВы ввели неверное значение...\n\n");
			break;
		}

		printf("\n");
	}
	free(recipeAdd);
	free(buff);
	free(fileName);
	free(Bonding);
	free(dir);
}

void addRecipe(struct Recipe* recipeAdd,
	char* fileName, char* Bonding, char* dir)
{
	strcpy(Bonding, "D:\\Book of recipes\\");
	printf("Введите имя рецепта:\n");
	fgets(fileName, 50, stdin);
	Sleep(500);

	char* nameRecipe[256];
	strcpy(nameRecipe, fileName);

	fileName[strlen(fileName) - 1] = '\0';

	strcat(fileName, ".recipe");
	mkdir(Bonding);
	strcpy(dir, Bonding);
	strcat(dir, fileName);

	FILE* newFile = fopen(dir, "wb");

	strcpy(recipeAdd->name, &nameRecipe);
	printf("Введите дату рецепта(дд.мм.гггг):\n");
	fgets(recipeAdd->date, 50, stdin);
	Sleep(500);
	printf("Введите рейтинг рецепта(1..10):\n");
	fgets(recipeAdd->rating, 50, stdin);
	Sleep(500);
	printf("Введите текст рецепта:\n");
	fgets(recipeAdd->text, 1024, stdin);
	Sleep(500);

	fwrite(recipeAdd, sizeof(struct Recipe), 1, newFile);
	printf("\nЗапись рецепта завершена.\n");
	fclose(newFile);
}

void showAllRecipe(char* Bonding)
{
	WIN32_FIND_DATAA found;
	HANDLE findResult = FindFirstFileA("D:\\Book of recipes\\*.recipe", &found);
	if (findResult == INVALID_HANDLE_VALUE)
	{
		printf("\nРецепты на диске отсутствуют !\n");
		return 1;
	}
	else
	{
		printf("Список рецептов:\n");
		do
		{
			printf(" - %s\n", found.cFileName);
		} while (FindNextFileA(findResult, &found));
	}
}

void viewRecipe(struct Recipe* buff,
	char* fileName, char* Bonding, char* dir)
{
	strcpy(Bonding, "D:\\Book of recipes\\");
	printf("Введите имя рецепта:\n");
	fgets(fileName, 50, stdin);
	fileName[strlen(fileName) - 1] = '\0';
	Sleep(500);


	strcat(fileName, ".recipe");
	mkdir(Bonding);
	strcpy(dir, Bonding);
	strcat(dir, fileName);

	FILE* openRecipe = fopen(dir, "r+b");
	if (openRecipe == NULL)
	{
		Sleep(500);
		printf("\nНету такого рецепта на диске!\n\n");
		return 1;
	}

	fread(buff, sizeof(struct Recipe), 1, openRecipe);
	printf("Название рецепта: %s", buff->name);
	printf("===============================================\n");
	printf("Дата создания: %s", buff->date);
	printf("===============================================\n");
	printf("Текст: %s", buff->text);
	printf("===============================================\n");
	printf("Рейтинг: %s", buff->rating);
	printf("===============================================\n");
	fclose(openRecipe);
}

void editRecipe(struct Recipe* buff,
	char* fileName, char* Bonding, char* dir)
{
	strcpy(Bonding, "D:\\Book of recipes\\");
	printf("Введите имя рецепта:\n");
	fgets(fileName, 250, stdin);
	fileName[strlen(fileName) - 1] = '\0';
	Sleep(500);

	strcat(fileName, ".recipe");
	mkdir(Bonding);
	strcpy(dir, Bonding);
	strcat(dir, fileName);

	FILE* openAndReductRecipe = fopen(dir, "r+b");
	if (openAndReductRecipe == NULL)
	{
		Sleep(500);
		printf("\nНету такого рецепта на диске!\n\n");
		return 1;
	}
	fread(buff, sizeof(struct Recipe), 1, openAndReductRecipe);
	fclose(openAndReductRecipe);

	printf("Введите текст рецепта:\n");
	fgets(buff->text, 1024, stdin);
	Sleep(500);

	FILE* reductRecipe = fopen(dir, "w+b");
	fwrite(buff, sizeof(struct Recipe), 1, reductRecipe);
	printf("\nОтредактировано...\n");
	fclose(reductRecipe);
}

void delReciep(char* fileName, char* Bonding, char* dir)
{
	strcpy(Bonding, "D:\\Book of recipes\\");
	printf("Введите имя рецепта:\n");
	fgets(fileName, 256, stdin);
	fileName[strlen(fileName) - 1] = '\0';
	Sleep(500);

	strcat(fileName, ".recipe");
	mkdir(Bonding);
	strcpy(dir, Bonding);
	strcat(dir, fileName);

	if (remove(dir) == -1)
	{
		printf("Нету рецепта с таким именем !\n");
	}
	else
	{
		printf("Рецепт успешно удалён...\n");
	}
}
