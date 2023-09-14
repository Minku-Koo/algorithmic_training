#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define MM 10001
#define MX 100000001
#define ML 100001

int v[ML] = {0};

int sol(int n, int lim){
	int ans = ML;
	int s=0, e=0, sums = v[s];
	
	while(s<n && e<n){
		if(sums >= lim){
			ans = min(ans, e-s+1);
		}
		
		if(sums >= lim){
			sums -= v[s];
			s++;
			if(s > e){
				sums += v[e+1];
				e++;
			}
		}
		else if(sums < lim){
			sums += v[e+1];
			e++;
		}
		
		if(ans == 1)
			return 1;
	}
	
	if(ans == ML) ans = 0;
	
	return ans;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n, lim, t;
	cin >> n >> lim;
	for(int i =0; i<n; i++){
		cin >> t;
		v[i] = t;
	}
	
	printf("%d", sol(n, lim));
	return 0;
}