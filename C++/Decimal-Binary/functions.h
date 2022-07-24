#include<stdio.h>
#include<conio.h>
#include<windows.h>
#include<math.h>
#include<stdlib.h>
#define abs(df) df < 0 ? -df : df
const char nonbin[]= "23456789";
void settitle(char* title)
{
	SetConsoleTitle(TEXT(title));
}
void entr(void){
	printf("\n\nPress Enter Key to Continue");
	while(getch()!='\r');
}
void showcursor(short int cnd) {
	HANDLE consoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
	CONSOLE_CURSOR_INFO info;
	info.dwSize = 5;
	info.bVisible = cnd;
	SetConsoleCursorInfo(consoleHandle, &info);
}
short check(char* ch,int l)
{
	for(int a = 0 ; a < l ; a++)
        {
            char h = ch[a];
            for(int b=0 ; b<9 ;b++)
                if(nonbin[b] == h)
                    return 1;
        }
	return 0;
}
void binr(long long int num){
	long long int d=0;
	int c=0,n=0;
	printf("\nBinary Conversion:\nSolution:-\n");
	while(num!=0)
	{
		c=num%2;
		printf("\n%c | %lld - %d", num!=1?'2':' ',num, c);
	    num = (num - c) / 2;
	    d = d + c * pow(10,n);
	    n++;
	}
	printf("\n\nOutput = %lld",d);
}
void decm(long long int nm){
	int b = log10(nm)+1, n;
	char* a =(char*) calloc(b , sizeof(char) );
	sprintf(a ,"%lld",nm);
	if (check(a,b))
	{
		printf("\n%lld is Not a Binary Number",nm);
		return;
	}
	long long int c = 0, d = 0;
	for (n = 0; n < b; n++)
	{
		c = (a[n] - 48) * pow(2, b - n - 1);
		d += c;
		printf("\n%c*2^%d = %lld", a[n], b - n - 1, c);
	}
	printf("\n\nOutput = %lld", d);
}