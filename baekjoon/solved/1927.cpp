#include <stdio.h>
#include <iostream>
#include <queue>

using namespace std;

#define M 100001

int n;
priority_queue<int, vector<int>, greater<int>> pq;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	queue<int> qq;
	cin >> n;
	
	for(int i=0; i<n; i++){
		int t;
		cin >> t;
		if(t == 0){
			if(pq.empty()){
				qq.push(0);
			}else{
				qq.push(pq.top());
				pq.pop();
			}
			
		}
		else{
			pq.push(t);
		}
	}
	
	while(!qq.empty()){
		printf("%d\n", qq.front());
		qq.pop();
	}
	
	return 0;
}