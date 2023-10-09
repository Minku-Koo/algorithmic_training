#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define MM 10000


int n;
int v[MM] = {0};

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	long long ans = 0, n, t;
	
	cin >> n;
	for(int i=0; i<n; i++){
		cin >> t;
		v[i] = t;
	}
	
	sort(v, v+n);
	
	//solve
	int idx = 0;
	for(register int i=0; i<n-1; i++){
		for(register int j=i+1; j<n-1; j++){
			int target = (v[i] +  v[j]) * -1;
			
			int large = upper_bound(v+j+1, v+n, target) -v;
			int small = lower_bound(v+j+1, v+n, target) -v;
			ans += large - small;
		}
	}
	
	printf("%lld", ans);
	return 0;
}