#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define MM 101

int n, ln;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0;
	
	cin >> n >> ln;
	vector<int> v[n+1];
	int a, b;
	for(int i=0; i<ln; i++){
		cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
	}
	
	// solve
	queue<int> qq;
	bool checked[n+1] = {0};
	qq.push(1);
	checked[1] = 1;
	
	while(!qq.empty()){
		int t = qq.front();
		qq.pop();
		
		for(int i=0; i<v[t].size(); i++){
			int p = v[t][i];
			if(checked[p]){
				continue;
			}
			ans++;
			checked[p] = 1;
			qq.push(p);
		}
	}
	
	printf("%d", ans);
	return 0;
}