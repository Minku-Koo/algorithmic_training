#include <stdio.h>

int atoi (char *str)
{
	int tot = 0;
    while(*str) {
        tot = tot * 10 + *str - '0'; 
        str++; 
    }
    
	return tot;
}


void itoa(int num, char* str)
{
	int i= 0;
    int deg= 1;
    int count= 0;
    int radix= 10;
	
    while(1){
    	if (num/deg)
        	count++;
        else
        	break;
        deg *= radix;
    }
	
    deg /= radix;
    
    while (i < count){
        *(str+i) = num/deg + '0'; 
        num -= ((num/deg) * deg); 
        deg /=radix; 
		i++;
    }
	
    *(str+i) = '\0';
	
}


int main(void){
	int n = 5432;
	char str[100];
	char ch[] = "7568";
	
	printf("%d \n", atoi(ch));
	itoa(n, str);
	printf("%s \n", str);
}

