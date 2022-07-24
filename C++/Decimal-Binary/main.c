#include "functions.h"

int main()
{
	long long int z=0;
	char a=0;
	showcursor(0);
	START:
        settitle("Decimal-Binary Converter");
	system("color 4f");
	system("cls");
	printf("1-Decimal to Binary\n2-Binary to Decimal\nPress ESC Key to Exit");
	while(1){
	a=getch();
	switch(a){
	        case '\x1b':
			goto EXIT;
			break;
		case '1':
			system("color 0f");
			system("cls");
                        settitle("Decimal To Binary");
			showcursor(1);
			printf("Enter a Decimal Number = ");
			scanf("%lld",&z);
			showcursor(0);
			binr(abs(z));
			entr();	
			z=0;		
			goto START;
			break;
		case '2':
			system("color 0f");
			system("cls");
                        settitle("Binary To Decimal");
			showcursor(1);
			printf("Enter a Binary Number = ");
			scanf("%lld",&z);
			showcursor(0);
			decm(abs(z));
			entr();
			z=0;  
			goto START;
			break;
         }
	}
	EXIT:
	return 0;
}
