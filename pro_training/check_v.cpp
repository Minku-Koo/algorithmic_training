
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int N;
int Firstchild[201];
int Secondchild[201];

int main(void)
{
	int i, test_case, addr;
	char str[200];
	int isoper = 0;
	for(test_case = 1; test_case <= 10; ++test_case)
	{
		int result = 1;
		memset(Firstchild, 0, sizeof(int) * 201);
		memset(Secondchild, 0, sizeof(int) * 201);

		scanf("%d", &N);
		for(i = 0; i < N; i++)
		{
			if(result==0) 
			{gets(str);
			continue;}
			
			scanf("%d", &addr);
			scanf("%s", str);
			isoper = 0;
			
			if( str[0]=='+' || str[0]=='-' || str[0]=='/' || str[0]=='*'  )
				isoper = 1;
			
			
			if(addr*2 <= N)
			{
				scanf("%d ",&Firstchild[addr]);
				if(addr*2 + 1 <= N)
					scanf("%d ",&Secondchild[addr]);
			}
			
			
			
			if(isoper==0){ // 중앙값이 숫자
				if(Firstchild[addr]!=0 || Secondchild[addr]!=0){
					result = 0;
					// scanf("%s", str);
					// break;
				}
			}else{ // 중앙값이 연산자
				if(Firstchild[addr]==0 || Secondchild[addr]==0){
					result = 0;
					// scanf("%s", str);
					// break;
				}
			}
			
		}

		// printf("#%d ", test_case);
		// int result = 1;
		
		printf("#%d %d\n", test_case, result);
		
	}

	return 0;//정상종료시 반드시 0을 리턴해야 합니다.
}
