#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> v;


int sol(int n, int k){
	int ans = 0, t = v[0];
	int s=0; int e=0;
	
	while(s<n && e<n){
		// t = _count(s, e);
		if(t > k){
			t -= v[s];
			if(e <= s){
				e++;
				if(e<n)
					t += v[e];
			}
				
			s++;
		}else{
			// t == k
			ans = max(ans, e-s+1);
			if(e != n-1)
				t += v[e+1];
			e++;
		}
		// printf("%d %d %d\n", s, e, t);
	}
	
	return ans;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, n, k, a, count_odd = 0;
	
	cin >> n >> k;
	for(int i=0; i<n; i++){
		cin >> a;
		if(a % 2 == 0)
			v.push_back(0);
		else{
			count_odd++;
			v.push_back(1);
		}
			
	}
	
	ans = sol(n, k);
	printf("%d", ans - min(count_odd, k));
	return 0;
}