#include <stdio.h>
#include <iostream>
#include <queue>
#include <vector>
#include <set>

using namespace std;

#define MM 51

int person_num, party_num;
vector<int> true_man;
set<int> connect[MM];
vector<int> party[MM];
bool checked[MM] = {0};

void bfs(int b){
	queue<int> qq;
	qq.push(b);
	checked[b] = 1;
	while(!qq.empty()){
		int p = qq.front();
		qq.pop();
		set<int>::iterator itr;
		for(itr = connect[p].begin(); itr != connect[p].end(); itr++){
			if(checked[*itr]){
				continue;
			}
			checked[*itr] = 1;
			qq.push(*itr);
		}
	}
	return;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0;
	
	cin >> person_num >> party_num;
	int t, p;
	cin >> t;
	for(int i=0; i<t; i++){
		cin >> p;
		true_man.push_back(p);
	}
	
	int temp;
	for(int i=0; i<party_num; i++){
		cin >> p;
		for(int j=0; j<p; j++){
			cin >> t;
			party[i].push_back(t);
			if(j>0){
				connect[t].insert(temp);
				connect[temp].insert(t);
			}
			temp = t;
		}
	}

	
	// true_man -> 모두 bfs 탐색 -> checked true 갱신
	for(int i=0; i<true_man.size(); i++){
		bfs(true_man[i]);
	}
	
	// 모든 party 탐색 -> checked true 있으면 out -> ans++
	for(int i=0; i<party_num; i++){
		int isflag = 1;
		for(int j=0; j<party[i].size(); j++){
			if(checked[party[i][j]] == 1){
				isflag = 0;
				break;
			}
		}
		if(isflag == 1){
			ans++;
		}
	}
	
	printf("%d", ans);
	return 0;
}