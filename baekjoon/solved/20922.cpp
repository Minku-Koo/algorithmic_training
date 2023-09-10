#include <stdio.h>
#include <iostream>
#include <algorithm>

#define M 200001
#define MN 100001

using namespace std;

int v[M] = {0};
int cnt[MN] = {0};

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 1, k, n, t, ln = 1;
	int s= 0, e = 0;
	
	// Input space
	cin >> k >> n;
	
	for(int i=0; i<k; i++){
		cin >> t;
		v[i] = t;
	}
	
	// zero index
	cnt[v[s]] += 1;
	
	while(true){
		if(e == k){
			ans = max(ans, e - s);
			break;
		}
		
		if(cnt[v[e]] > n){
			ans = max(ans, e - s);
			cnt[v[s]] -= 1;
			s++;
		}else{
			e++;
			cnt[v[e]] += 1;
		}
		
	}
	
	printf("%d", ans);
	return 0;
}