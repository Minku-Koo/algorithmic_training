#include <stdio.h>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MM 1002

int n, m;
vector<int> v[MM];
int leg[MM] = {0};
int result[MM] = {0};

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, t, q, temp;
	
	cin >> n >> m;
	for(int i=0; i<m; i++){
		cin >> t;
		for(int s=0; s<t; s++){
			cin >> q;
			if(s > 0){
				v[temp].push_back(q);
				leg[q]++;
			}
			temp = q;
		}
	}
	
	// solve
	queue<int> qq;
	for(int i=1; i<=n; i++){
		if(leg[i]==0){
			qq.push(i);
		}
	}
	
	for(int i=1; i<=n; i++){
		if(qq.empty()){
			printf("0\n");
			return 0;
		}
		int tt = qq.front();
		qq.pop();
		result[i-1] = tt;
		for(int j=0; j<v[tt].size(); j++){
			leg[v[tt][j]]--;
			if(leg[v[tt][j]] == 0){
				qq.push(v[tt][j]);
			}
		}
	}
	
	for(int i=1; i<=n; i++){
		printf("%d\n", result[i-1]);
	}
	
	return 0;
}