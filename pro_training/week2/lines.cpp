//
//
#include<iostream>
#include<string.h>
#include<queue>
#include<vector>
#define MAX 50001
using namespace std;

// int arr[MAX][MAX];
vector<int> arr[MAX];
int visit[MAX];

void solution(int num, int count){
	queue<int> enter;
	queue<int> dq;
	// 진입차수 0인것
	for(int j=0; j<count; j++){
		if(visit[j]==0) enter.push(j);
	}
	
	// enter가 빌때까지 계속 반복
	// enter에서 나가는 부분 enter에 넣고, dequeue에 삽입
	while(!enter.empty()){
		int node = enter.front();
		dq.push(node);
		enter.pop();
		
		for(int j=0; j<num; j++){
			// if(arr[node][j]==1)
		for(int v=0; v<arr[node].size(); v++)
			if(arr[node][v]==j)
				enter.push(j);
		}
	}
	
	while(!dq.empty()){
		printf(" %d", dq.front());
		dq.pop();
	}
	
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	
	cin>>T;
	
	int n, m, a, b;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d", &n, &m);
		for (int i = 0; i < MAX; i++) 
			arr[i].clear();

		// arr[MAX][MAX] = {0,};
		visit[MAX] = {0,};
		
		for(int k=0; k<m; k++){
			scanf("%d %d", &a, &b);
			visit[b]++ ;
			// arr[a][b] =1;
			arr[a].push_back(b);
		}
		
		printf("#%d", test_case);
		solution(n, m);
		printf("\n");
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}