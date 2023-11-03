#include <stdio.h>
#include <iostream>
#include <queue>

using namespace std;

struct Node{
	int t, c;
};

struct cmp{
	bool operator()(const Node &a, const Node &b){
		if(a.t == b.t){
			return a.c < b.c;
		}
		return a.t > b.t;
	}
};

priority_queue<Node, vector<Node>, cmp> pq;
priority_queue<int, vector<int>, greater<int>> pqq;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, n, a, b;
	
	cin >> n;
	for(int i=0; i<n; i++){
		cin >> a >> b;
		Node nd = {a, b};
		pq.push(nd);
	}
	
	// solve
	int cnt = 0;
	while(!pq.empty()){
		Node nod = pq.top();
		if(nod.t > cnt){
			pqq.push(nod.c);
			cnt++;
		}else{
			if(!pqq.empty() && (pqq.top() < nod.c)){
				pqq.pop();
				pqq.push(nod.c);
			}
		}
		pq.pop();
	}
	
	while(!pqq.empty()){
		ans += pqq.top();
		pqq.pop();
	}
	
	printf("%d", ans);
	return 0;
}