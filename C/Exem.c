#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <locale.h>

#define SizeName 256
#define SizeText 1024

enum Recipe
{
	RecipeAdd = 1,
	RecipeView,
	RecipeEditing,
	RecipeDeleting,
	Exit
}recipe;

struct RecipeInfo
{
	int DateOfRecipe;
	char RecipeName[SizeName];
	char RecipeText[SizeText];
	int Rating;
};

void printMenu()
{
	printf("\tМеню:\n");
	printf("1.Добавление рецепта\n");
	printf("2.Просмотр рецепта\n");
	printf("3.Редактирование рецепта\n");
	printf("4.Удаление рецепта\n");
	printf("5.Выход\n");
	scanf("%i", &recipe);
}

void printRecipeInfo(struct RecipeInfo* recipeInfo)
{
	printf("1.Дата создания рецепта:\t%i\n", recipeInfo->DateOfRecipe);
	printf("2.Имя рецепта:\t%s\n", recipeInfo->RecipeName);
	printf("3.Текст рецепта:\t%s\n", recipeInfo->RecipeText);
	printf("4.Рейтинг(от1 до10):\t%i\n", recipeInfo->Rating);
	
}

void AddRecipe(struct RecipeInfo* recipeInfo,FILE* RecipeFile)
{
		printf("Введите имя рецепта: ");
		scanf("%s", &recipeInfo->RecipeName);
		strcat(recipeInfo->RecipeName, ".recipe");
		RecipeFile = fopen(recipeInfo->RecipeName, "w");
		printf("Введите текст рецепта: ");
		scanf("%s", &recipeInfo->RecipeText);
		fputs(recipeInfo->RecipeText, RecipeFile);
		fclose(RecipeFile);
		printf("Рейтинг рецепта %s (от1 до10): ", recipeInfo->RecipeName);
		scanf("%i", &recipeInfo->Rating);
}

int main()
{
	setlocale(LC_ALL, "rus");
	struct RecipeInfo* recipeInfo = malloc(sizeof(struct RecipeInfo));
	FILE* RecipeFile;
	printMenu();

	while (true)
	{
		switch (recipe)
		{
		case RecipeAdd:
			AddRecipe(recipeInfo, &RecipeFile);
			break;
		case RecipeView:
			printRecipeInfo(recipeInfo);
			break;
		case RecipeEditing:
			break;
		case RecipeDeleting:
			break;
		case Exit:
			exit(0);
		default:
			printf("Не верный выбор,попробуй снова.\n");
			break;
		}
		printf("\n");
		printMenu();
	}
}
