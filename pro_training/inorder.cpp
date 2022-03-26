//

#include <stdio.h>
#include <string.h>

struct Node{
	char data;
	int left=0;
	int right=0;
};

Node arr[101];

void inorder(int n){
	Node node = arr[n];
	if(node.left!=0) inorder(node.left);
	printf("%c", node.data);
	if (node.right!=0) inorder(node.right);
	return ;
}


void preorder(int n){
	Node node = arr[n];
	printf("%c", node.data);
	if(node.left!=0) preorder(node.left);
	if (node.right!=0) preorder(node.right);
	return ;
}

void postorder(int n){
	Node node = arr[n];
	if(node.left!=0) postorder(node.left);
	if (node.right!=0) postorder(node.right);
	printf("%c", node.data);
	return ;
}



int N;
char Alpha[101];
int Firstchild[101];
int Secondchild[101];

int main(void)
{
	int test_case;
	for(test_case = 1; test_case <= 10; ++test_case) {
		int i, j;
		int addr;
		char str[1000];
		memset(Firstchild, 0, sizeof(int) * 101);
		memset(Secondchild, 0, sizeof(int) * 101);
		memset(Alpha, 0, sizeof(char) * 101);
		
		scanf("%d", &N);
		for(i = 0; i < N; i++) {
			scanf("%d", &addr);
			scanf("%s", str);

			Alpha[addr] = str[0];
			if(addr*2 <= N) {
				scanf("%d ",&Firstchild[addr]);
				if(addr*2 + 1 <= N) scanf("%d ",&Secondchild[addr]);
			}
			
			arr[addr].data = Alpha[addr];
			arr[addr].left = Firstchild[addr];
			arr[addr].right = Secondchild[addr];
		}
		printf("#%d ", test_case);
		inorder(1);
		printf("\n");
	}

	return 0;
}
