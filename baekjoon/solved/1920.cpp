#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define MM 100001

long long v[MM] = {0};

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, n, m;
	long long t;
	
	cin >> n;
	for(int i=0; i<n; i++){
		cin >> t;
		v[i] = t;
	}
	
	sort(v, v+n);
	
	// solve
	cin >> m;
	for(int i=0; i<m; i++){
		cin >> t;
		int s=0, m, e=n-1, ans =0;
		while(s<=e){
			m = (s+e)/ 2;
			if(v[m] == t){
				ans = 1;
				break;
			}
			
			if(v[m] < t)
				s = m+1;
				
			if(v[m] > t)
				e = m -1;
		}
		
		
		printf("%d\n", ans);
	}
	
	return 0;
}