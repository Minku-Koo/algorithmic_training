#include <stdio.h>
#include <iostream>
#include <math.h>

using namespace std;

#define MM 100001

long long v[MM] = {0};
long long MX = 100000001 * 2;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	long long ans = MX, t;
    int n;
	
	cin >> n;
    for(int i=0; i<n; i++){
        cin >> t;
        v[i] = t;
    }

    // solve
    // two pointer

    int s =0, e =n-1;
    while(s<e){
        int sm = v[s] + v[e];
        if(sm == 0){
            ans = 0;
            break;
        }

        if(sm < 0){
            s++;
        }
        else{
            e--;
        }
        
        if(abs(sm) < abs(ans)){
            ans = sm;
        }
    }
    

	printf("%lld", ans);
	return 0;
}