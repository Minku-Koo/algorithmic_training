#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define MM 1001

long long MX = 200000000;
long long ln, t;
long long v[MM] = {0};


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	
    // input
	cin >> ln;
	for(int i=0; i<ln; i++){
        cin >> t;
        v[i] = t;
    }

    // solve
    sort(v, v+ln);
    
    for(long long  i=ln-1; i>=0; i--){
        // 제일 큰 수부터 finding
        int s = 0, m, e = i-1;
        long long numSum, target = v[i];
        // printf("target %lld \n", target);
        while(s<=e){
            m = (s+e) / 2;
            // if(m==s || m==e) break;
            numSum = v[s] + v[m] + v[e];
            // printf("s %d m %d e %d numSUm %d\n", s, m, e, numSum);
            if(numSum<target){
                if(s < m)
                    s = m;
                else
                    s = m + 1;
            }else if(numSum>target){
                if(e > m)
                    e = m;
                else
                    e = m - 1;
            }else{ // numSum == target
                printf("%lld", target);
                return 0;
            }

            if(m==s && m==e) break;
        }

    }

	return 0;
}