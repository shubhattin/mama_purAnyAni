#include "functions.h"

int main()
{
	int s,m,h;
	char a,b;
	hidecursor();
	SetConsoleTitle(TEXT("Stopwatch"));
	system("color 90");
	locate(10,28);
	printf("Featured Stopwatch\n\t\t\tMade by Shubham Anand Gupta");
	Beep(450,700);
	START:
	s = 0;
	h = 0;
	m = 0;
	b = '\0';
	a = '\0';
	system("cls");
	system("color 0e");
	locate(2,5);
	printf("Press Enter Key To Start Stopwatch");
	while (getch() != '\r');
	system("cls");
	system("color 0f");
	CONT:
	a=key();
	if(a=='1')
	{
		locate(11,1);
		printf("1-Resume");
		system("color 0a");
		while(1)
		{
			b=getch();
			if(b=='1')
			{
				system("color 0f");
			    goto CONT;
			}
		    if(b=='2')
				goto START;
		    if(b=='\x1b')
				goto EXIT;
		}
	}
	if(a=='2')
		goto START;
	if(a=='\x1b')
		goto EXIT;
	Sleep(1000);
	s++;
	if(s==60)
	{
		m++;
		s=0;
	}
	if(m==60)
	{
		h++;
		m=0;
	}
	locate(10,15);
	printf("%d hours: %d minutes: %d seconds",h,m,s);
	locate(11,1);
	printf("1-Pause ");
	locate(12,1);
	printf("2-Reset");
	locate(13,1);
	printf("Press ESC Key to Exit\n");
	goto CONT;
    EXIT:
	Beep(400, 500);
	return 0;
}
