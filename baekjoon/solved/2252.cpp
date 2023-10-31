#include <stdio.h>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define MM 32001
#define MX 100001

vector<int> v[MM];
int leg[MM] = {0};
int result[MM] = {0};

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, n, m;
	
	cin >> n >> m;
	
	int a,b;
	for(int i=0; i<m; i++){
		cin >> a >> b;
		v[a].push_back(b);
		leg[b] += 1;
	}
	
	// solve
	queue<int> qq;
	for(int i=1; i<=n; i++){
		if(leg[i] == 0){
			qq.push(i);
		}
	}
	
	for(int i=1; i<=n; i++){
		int t = qq.front();
		qq.pop();
		result[i-1] = t;
		for(int j=0; j<v[t].size(); j++){
			int p = v[t][j];
			leg[p] -= 1;
			if(leg[p] == 0){
				qq.push(p);
			}
		}
	}
	
	for(int i=0; i<n; i++){
		printf("%d ", result[i]);
	}

	return 0;
}