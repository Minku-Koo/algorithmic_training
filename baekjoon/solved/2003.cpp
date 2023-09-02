#include <stdio.h>
#include <iostream>

using namespace std;

#define MM 10001

int v[MM] = {0,};

int sol(int n, int m){
	int ans = 0;
	int s = 0, e = 0, t = v[0];
	
	while(s <n && e<n){
		if(t >= m){
			if(t == m){
				ans++;
				if(e < n-1)
					t += v[e+1];
				e++;
			}
			t -= v[s];
			s++;
		}else{
			// t < m
			if(e < n-1)
				t += v[e+1];
			e++;
		}
	}
	
	return ans;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, a, n, m;
	
	cin >> n >> m;
	for(int i=0; i<n; i++){
		cin >> a;
		v[i] = a;
	}
	
	printf("%d", sol(n, m));
	return 0;
}