

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int N;
char Oper[201];
int Firstchild[201];
int Secondchild[201];
int Num[201];

int main(void)
{
	int test_case;
	
	for(test_case = 1; test_case <= 10; ++test_case)
	{
		int i, j;
		int addr;
		char str[200];
		memset(Firstchild, 0, sizeof(int) * 201);
		memset(Secondchild, 0, sizeof(int) * 201);
		memset(Num, 0, sizeof(int) * 201);
		memset(Oper, 0, sizeof(char) * 201);

		scanf("%d", &N);
		for(i = 0; i < N; i++)
		{
			scanf("%d", &addr);
			scanf("%s", str);

			if( strcmp(str,"+") == 0 || strcmp(str,"-")== 0  || strcmp(str,"/") == 0 || strcmp(str,"*")== 0  )
			{
				Oper[addr] = str[0];
			}
			else{
				Num[addr] = atoi(str);
			}
			
			if(addr*2 <= N)
			{
				scanf("%d ",&Firstchild[addr]);
				if(addr*2 + 1 <= N)
					scanf("%d ",&Secondchild[addr]);
			}
			
		}


		printf("#%d ", test_case);
		int result = 1;
		
		for(register int i=0; i<N; i++){
			if(Oper[i]==0){ // 중앙값이 숫자
				if(Firstchild[i]!=0 || Secondchild[i]!=0){
					result = 0	;
					break;
				}
			}else{ // 중앙값이 연산자
				if(Firstchild[i]==0 || Secondchild[i]==0){
					result = 0	;
					break;
				}
			}
		}
		
		printf("%d\n", result);
	}

	return 0;//정상종료시 반드시 0을 리턴해야 합니다.
}




// #1 0
// #2 0
// #3 0
// #4 1
// #5 0
// #6 1
// #7 1
// #8 0
// #9 0
// #10 0