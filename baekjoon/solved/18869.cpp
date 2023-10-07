#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

#define MH 10001
#define MV 101

vector<pair<int, int>> v[MV];  // number, index

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, n, m, t;
	
	cin >> n >> m;
	
	for(int i=0; i<n; i++){
		int idx = 0;
		for(register int j=0; j<m; j++){
			cin >> t;
			v[i].push_back({t, idx++});
		}
	}
	
	// solve
	for(register int i=0; i<n; i++){
		sort(v[i].begin(), v[i].end());
	}
	
	for(int i=0; i<n; i++){
		for(register int j=i+1; j<n; j++){
			for(register int a=0; a<m; a++){
				if(v[i][a].second == v[j][a].second){
					if(a < m-1){
						// 처음부터 정렬된 경우
						if((v[i][a].first < v[i][a+1].first) !=
							(v[j][a].first < v[j][a+1].first)){
							break;
						}
					}else{
						ans++;
					}
				}else{
					break;
				}
			}
		}
	}
	
	
	printf("%d", ans);
	return 0;
}