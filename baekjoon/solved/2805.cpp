#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define TREE_MAX 2000000001
#define TREE_CNT 1000001

long long v[TREE_CNT] = {0};
long long treeCnt, k;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	long long ans = 0, t, treeMax = 0;
	
	cin >> treeCnt >> k;
	for(int i=0; i<treeCnt; i++){
		cin >> t;
		v[i] = t;
		if(treeMax < t){
			treeMax = t;
		}
	}
	
	// solve
	long long s=0, e=treeMax;
	long long m;
	
	while(s<=e){
		m = (s + e) /2;
		long long treeSum = 0;
		for(int i=0; i<treeCnt; i++){
			long long temp = v[i] - m;
			if(temp > 0){
				treeSum += temp;
			}
		}
		if(treeSum >= k){
			ans = max(ans, m);
			s = m+1;
		}
		else{
			e = m-1;
		}
	}
	
	
	printf("%d", ans);
	return 0;
}