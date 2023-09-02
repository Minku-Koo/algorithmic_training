#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

#define MM 100001

int checked[MM] = {0,};
int v[MM] = {0,};
long long ans = 0;

void sol(int n){
	
	int s=0, e=0;
	
	
	for(s=0; s<n; s++){
		for(; e<n; e++){
			if(checked[v[e]] == 0){
				checked[v[e]] = 1;
			}else{  // init
				break;
			}
		}
		ans += (e - s);
		checked[v[s]] = 0;
	}
	
	return ;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int	a, n;
	
	cin >> n;
	for(int i=0; i<n; i++){
		cin >> a;
		v[i] = a;
	}
	sol(n);
	printf("%lld", ans);
	return 0;
}