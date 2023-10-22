#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define M 501
#define MM 10001

int n, m;

struct Node{
	int num, dist;
};

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0;
	
	cin >> n >> m;
	
	int a, b;
	vector<int> v[n+1];
	for(int i=0; i<m; i++){
		cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
	}
	
	// solve
	queue<Node> qq;
	bool checked[n+1] = {0};
	qq.push({1, 0});
	checked[1] = 1;
	
	while(!qq.empty()){
		Node t = qq.front();
		qq.pop();

		for(int i=0; i<v[t.num].size(); i++){
			int q = v[t.num][i];
			
			if(checked[q])
				continue;

			ans++;
			checked[q] = 1;
			if(t.dist >= 1)
				continue;

			qq.push({q, t.dist+1});
			
		}
	}
	
	printf("%d", ans);
	return 0;
}