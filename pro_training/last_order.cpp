//
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int N;
char Operator[1001];
// int Firstchild[1001];
// int Secondchild[1001];
int Number[1001];

struct Node{
	int opr_num;
	int left=0;
	int right=0;
};

int cnt;
Node arr[1001];

int calc(char op, int a, int b){
	if(op=='-')  a-=b;
	else if(op=='+') a+=b;
	else if(op=='*') a*=b;
	else a/=b;
	return a;
}

void solution(int n){
	Node node = arr[n];
	int ln = node.left;
	if(ln!=0) solution(ln);
	if(node.opr_num==0 &&
		(arr[ln].left==0 && arr[ln].right==0 ) &&
		(arr[node.right].left==0 && arr[node.right].right==0 ) 
		) {
		arr[n].opr_num = 1;
		Number[n] = calc(Operator[n], Number[ln], Number[node.right]);
		arr[n].left = 0;
		arr[n].right = 0;
		cnt+=2;
	}
	
	if (node.right!=0) solution(node.right);
	return ;
}

int main(void)
{
	int test_case;
	
	setbuf(stdout, NULL);
	
	for(test_case = 1; test_case <= 10; ++test_case)
	{
		cnt=0;
		int addr, fn, sn;
		char str[1000];
		arr[101] = {0};
		
		// memset(Firstchild, 0, sizeof(int) * 1001);
		// memset(Secondchild, 0, sizeof(int) * 1001);
		memset(Number, 0, sizeof(int) * 1001);
		memset(Operator, 0, sizeof(char) * 1001);
		
		scanf("%d", &N);
		for(register int i = 0; i < N; i++) {
			scanf("%d", &addr);
			scanf("%s", str);
			if( strcmp(str,"+") == 0 || strcmp(str,"-")== 0  || strcmp(str,"/") == 0 || strcmp(str,"*")== 0  )
			{
				Operator[addr]=str[0];	
				scanf("%d %d", &fn, &sn);
				arr[addr].opr_num = 0;
			}
			else {
				Number[addr]=atoi(str);
				arr[addr].opr_num = 1;
				fn=0; sn=0;
			}
			
			arr[addr].left = fn;
			arr[addr].right = sn;
		}

		while(cnt+1!=N) solution(1);
		printf("#%d %d\n", test_case, Number[1]);
	}

	return 0; 
}
