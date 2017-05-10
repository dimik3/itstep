#include <stdio.h>
#include <stdbool.h>
#include <Windows.h>

#define LOG_FN_START(arg) printf("[%d] %s\n", time(0),#arg  " start");
#define LOG_FN_END(arg) printf("[%d] %s\n", time(0),#arg  " end");

//# Преврощает аргумент в двойные скобки. arg (foo) -> #arg = "foo"


void foo();
void foo1();

void foo()
{
	LOG_FN_START(foo)

	Sleep(1000);
	foo1();

	LOG_FN_END(foo)
}

void foo1()
{
	LOG_FN_START(foo1)

	Sleep(1000);

	LOG_FN_END(foo1)
}

int main()
{
	LOG_FN_START(foo)

	foo();

	LOG_FN_END(foo)
}
