#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define MM 1000001

int v[MM] = {0};
int childCnt, n, lenMax = 0;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, t;
	
	cin >> childCnt >> n;
	for(int i=0; i<n; i++){
		cin >> t;
		v[i] = t;
		if(lenMax < t){
			lenMax = t;
		}
	}
	
	// solve 
	int s=1, e=lenMax, m, tempCnt;
	while(s <= e){
		m = (s+e) / 2;
		tempCnt = 0;
		for(register int i=0; i<n; i++){
			if(v[i] / m >= 0){
				tempCnt += v[i] / m ;
			}
		}
		
		if(tempCnt >= childCnt){
			ans = max(ans, m);
			s = m+1;
		}else{
			e = m-1;
		}
	}
	
	printf("%d", ans);
	return 0;
}