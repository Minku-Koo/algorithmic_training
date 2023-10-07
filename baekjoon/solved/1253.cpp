#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define MM 2001
long long v[MM] = {0};

int solve(int ln, int n){
    int s=0, e=ln-1;
    while(s<e){
        if(e == n) {
            e--; continue;
        }
        if(s == n) {
            s++; continue;
        }

        long long ssum = v[s] + v[e];
        
        if(ssum > v[n]){
            e--;
        }else if(ssum < v[n]){
            s++;
        }else {
            return 1;
        }
    }
    return 0;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, n, t;
	
	cin >> n;
    for(int i=0; i<n; i++){
        cin >> t;
        v[i] = t;
    }
    
    //solve
    sort(v, v+n);

    for(int i=0; i<n; i++){
        ans += solve(n, i);
    }

	printf("%d", ans);
	return 0;
}