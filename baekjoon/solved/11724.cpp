#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define MM 1001

int n, m;
bool checked[MM] = {0};


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0;
	
	cin >> n >> m;
	vector<int> v[n+1];
	
	int x, y;
	for(int i=0; i<m; i++){
		cin >> x >> y;
		v[x].push_back(y);
		v[y].push_back(x);
	}
	
	// solve
	
	for(int i=1; i<=n; i++){
		
		// checked에 있으면 continue
		if(checked[i]){
			continue;
		}

		// 첫노드 qq에 삽입
		queue<int> qq;
		qq.push(i);
		checked[i] = 1;
		
		// while qq
		while(!qq.empty()){
			int node = qq.front();
			qq.pop();
			
			
			for(int j=0; j<v[node].size(); j++){
				if(checked[v[node][j]]){
					continue;
				}
				qq.push(v[node][j]);
				checked[v[node][j]] = 1;
			}
		}
		ans++;
		
	}
	
	printf("%d", ans);
	return 0;
}