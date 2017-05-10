#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#include <stdbool.h>
#include <direct.h>


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
Пункт №1 спрашивает имя рецепта на английском языке (или транслите). Это имя в
последствии будет именем файла на файловой системе в котором будет лежать весь тест.
Расширение файла - *.recipe. Далее программа спрашивает текст рецепта и рейтинг.
Пункт №2 выводит список рецептов на файловой системе (файлы с маской *.recipe рядом
с приложением) у которых размер файла больше 0. Далее выводит на экран содержимое
рецепта (дата, имя, текст, рейтинг).
Пункт №3 выводит список рецептов на файловой системе (файлы с маской *.recipe рядом
с приложением) у которых размер файла больше 0. Затем программа спрашивает новый
текст рецепта, который заменит весь текущий текст.
Пункт №4 выводит список рецептов на файловой системе (файлы с маской *.recipe рядом
с приложением), затем спрашивает какой из тестов надо удалить и очищает файл (размер
0).
Пункт №5 – выход из программы.
Очистка файла: можно открыть файл в режиме "w" и закрыть.
*/


struct Recipe
{
	char* name[50];
	char* date[30];
	char* text[1024];
	char* rating[10];
};


enum Menu
{
	AddRecipe = '1',
	VieRecipe = '2',
	EditRecipe = '3',
	DelReciep = '4',
	Exit = '0',
};

void Recipe(struct Recipe recipe[]);
void FileNull(FILE* fp);

int main()
{
	setlocale(LC_ALL, "rus");
	struct Recipe* recipe = malloc(1024 * sizeof(struct Recipe));	
	printf("\t\t =*=*=*=*=*=*= Книга рецептов =*=*=*=*=*=*= \n\n");
	Recipe(recipe);
	return 0;
}

void FileNull(FILE* fp)
{
	if (fp == NULL)
	{
		printf("Не удалось открыть файл!\n");
		getch();
		exit(0);
	}
}

void Recipe(struct Recipe recipe[])
{
	char* fileName = (char *)malloc(200);
	char* disk = (char *)malloc(200);
	char* folderName = (char *)malloc(200);
	char* Bonding = (char *)malloc(200);
	char* dir = (char *)malloc(200);

	while (true)
	{
		printf("Выберите пункт меню:\n");
		printf("1 - Добавить рецепт\n2 - Просмотр рецепта\n3 - Редактирование рецепта\n4 - Удаление рецепта\n0 - Выход\n");
		FILE* fp;
		char pressKey = getch();
		switch (pressKey)
		{
		case AddRecipe:
			printf("Введите имя диска:\n");
			fgets(disk, 50, stdin);
			printf("Введите имя папки:\n");
			fgets(folderName, 50, stdin);
			printf("Введите имя рецепта:\n");
			fgets(fileName, 50, stdin);

			char* nameRecipe[256];
			strcpy(nameRecipe, fileName);

			disk[strlen(disk) - 1] = '\0';
			folderName[strlen(folderName) - 1] = '\0';
			fileName[strlen(fileName) - 1] = '\0';

			strcpy(Bonding, disk);
			strcat(Bonding, ":\\");
			strcat(Bonding, folderName);
			strcat(fileName, ".recipe");
			mkdir(Bonding);
			strcpy(dir, Bonding);
			strcat(dir, "\\");
			strcat(dir, fileName);

			fp = fopen(dir, "w");
			FileNull(fp);

			strcpy(recipe->name, &nameRecipe);
			printf("Введите дату рецепта(дд.мм.гггг):\n");
			fgets(recipe->date, 50, stdin);
			printf("Введите рейтинг рецепта(1..10):\n");
			fgets(recipe->rating, 50, stdin);
			printf("Введите текст рецепта:\n");
			fgets(recipe->text,1024,stdin);

			fwrite(recipe,sizeof(struct Recipe),1,fp);
			fclose(fp);
			break;

		case VieRecipe:
			printf("Введите имя диска:\n");
			fgets(disk, 50, stdin);
			printf("Введите имя папки:\n");
			fgets(folderName, 50, stdin);
			printf("Введите имя рецепта:\n");
			fgets(fileName, 50, stdin);

			disk[strlen(disk) - 1] = '\0';
			folderName[strlen(folderName) - 1] = '\0';
			fileName[strlen(fileName) - 1] = '\0';

			strcpy(Bonding, disk);
			strcat(Bonding, ":\\");
			strcat(Bonding, folderName);
			strcat(fileName, ".recipe");
			mkdir(Bonding);
			strcpy(dir, Bonding);
			strcat(dir, "\\");
			strcat(dir, fileName);

			fp = fopen(dir, "r");
			FileNull(fp);

			fread(recipe, sizeof(struct Recipe),1,fp);
			printf("Имя рецепта: %s", recipe->name);
			printf("===============================================\n");
			printf("Дата рецепта: %s\n", recipe->date);
			printf("===============================================\n");
			printf("Текст: \n%s\n", recipe->text);
			printf("===============================================\n");
			printf("Рейтинг: %s", recipe->rating);
			printf("===============================================\n");
			fclose(fp);
			break;

		case EditRecipe:
			printf("Введите имя диска:\n");
			fgets(disk, 50, stdin);
			printf("Введите имя папки:\n");
			fgets(folderName, 50, stdin);
			printf("Введите имя рецепта:\n");
			fgets(fileName, 250, stdin);

			disk[strlen(disk) - 1] = '\0';
			folderName[strlen(folderName) - 1] = '\0';
			fileName[strlen(fileName) - 1] = '\0';

			strcpy(Bonding, disk);
			strcat(Bonding, ":\\");
			strcat(Bonding, folderName);
			strcat(fileName, ".recipe");
			mkdir(Bonding);
			strcpy(dir, Bonding);
			strcat(dir, "\\");
			strcat(dir, fileName);

			fp = fopen(dir, "w");
			FileNull(fp);
			
			printf("Введите дату рецепта(дд.мм.гггг):\n");
			fgets(recipe->date, 50, stdin);
			printf("Введите рейтинг рецепта(1..10):\n");
			fgets(recipe->rating, 50, stdin);
			printf("Введите текст рецепта:\n");
			fgets(recipe->text, 1024, stdin);
			
			fwrite(recipe, sizeof(struct Recipe), 1, fp);
			fclose(fp);
			break;

		case DelReciep:
			printf("Введите имя диска:\n");
			fgets(disk, 50, stdin);

			printf("Введите имя папки:\n");
			fgets(folderName, 256, stdin);

			printf("Введите имя рецепта:\n");
			fgets(fileName, 256, stdin);

			disk[strlen(disk) - 1] = '\0';
			folderName[strlen(folderName) - 1] = '\0';
			fileName[strlen(fileName) - 1] = '\0';

			strcpy(Bonding, disk);
			strcat(Bonding, ":\\");
			strcat(Bonding, folderName);
			strcat(fileName, ".recipe");
			mkdir(Bonding);
			strcpy(dir, Bonding);
			strcat(dir, "\\");
			strcat(dir, fileName);

			FileNull(fp);
			if (remove(dir) == -1)
			{
				printf("Ошибка!\n");
			}
			else
			{
				printf("Удалено..\n");
			}
			break;
		case Exit:
			return 0;
			break;
		default:
			printf("\nВы ввели неверное значение...\n\n");
			break;
		}

		printf("\n");
	}
	free(fileName);
	free(disk);
	free(folderName);
	free(Bonding);
	free(dir);
}
