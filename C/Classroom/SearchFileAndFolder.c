#include <Windows.h>
#include <stdio.h>
#include <stdbool.h>
 
int main()
{
    WIN32_FIND_DATAA found;
    HANDLE findResult =
        FindFirstFileA(
            "d:\\winners\\*.jpg",
            &found);
 
    if (findResult == INVALID_HANDLE_VALUE)
    {
        printf("Files not found.");
        return 1;
    }
    // WinAPI
    do
    {
        if (strcmp(found.cFileName, ".") == 0 ||
            strcmp(found.cFileName, "..") == 0)
        {
            continue;
        }
       
        SYSTEMTIME time;
        FileTimeToSystemTime(
            &found.ftLastAccessTime, &time);
        printf("[%d.%d.%d] ", time.wDay, time.wMonth, time.wYear);
        bool isDirectory =
            found.dwFileAttributes &
            FILE_ATTRIBUTE_DIRECTORY;
        printf("%s found: \"%s\".\n",
            (isDirectory ? "Folder" : "File"),
            found.cFileName);
    } while (FindNextFileA(findResult,
        &found));
 
    FindClose(findResult);
}
