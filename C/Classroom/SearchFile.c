#include <stdio.h>
#include <windows.h>

int main()	
{
	
	WIN32_FIND_DATAA found;
	HANDLE findResult = FindFirstFileA("D:\\*.txt", &found);
	if (findResult == INVALID_HANDLE_VALUE)
	{
		printf("Files not found");
		return 1;
	}
	printf("File found: %s \n", found.cFileName);

	while (FindNextFileA(findResult,
		&found))
	{
		printf("File found: %s \n", found.cFileName);
	}
}
