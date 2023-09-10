#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define MM 1000002

struct Pos{
	int x, y;
};

Pos v[MM] = {0};
int cnt[MM] = {0};
int s, e;

int solve(int ls, int rs, int n, int k){
	int ans = 0;
	s = 0; e = 0;
	
	while (n--) {
		Pos p = v[n];
		for (int i = p.x+1;i <= p.y;i++) {
			cnt[i]++;
		}
	}
	
	while(e <= MM){
		if(ans == k){
			return 1;
		}
		if(ans > k){
			s++;
			ans -= cnt[s];
		}else if(ans < k){
			e++;
			ans += cnt[e];
		}
	}
	
	return 0;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, n, k, x, y;
	int ls = MM, rs = 0;
	
	cin >> n >> k;
	
	for(int i =0; i<n; i++){
		cin >> x >> y;
		ls = min(x, ls);
		rs = max(y, rs);
		v[i] = {x, y};
	}
	
	ans = solve(ls, rs, n, k);
	
	if(ans == 0)
		printf("%d %d", 0 ,0);
	else 
		printf("%d %d", s, e);
	return 0;
}