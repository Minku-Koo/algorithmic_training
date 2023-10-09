#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define MM 1001

long long target;
int n, m;
long long va[MM], vb[MM];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, t;
	
    cin >> target;
	cin >> n;
    for(int i=0; i<n; i++){
        cin >> t;
        va[i] = t;
    }
    
	cin >> m;
    for(int i=0; i<m; i++){
        cin >> t;
        vb[i] = t;
    }
    
    // solve

    int as=0, ae=0;
    long long a_sum = va[as] ;
    while(as<n && ae<n){
        
        long long new_target = target - a_sum;
        // ****** find vb
        int bs=0, be=0;
        long long b_sum = vb[bs];
        printf("as %d ae %d new_target %d\n", as, ae, new_target);
        if(new_target > 0){
            while(bs<m && be<m){
                printf("bs %d be %d b_sum %d \n", bs, be, b_sum);
                if(b_sum > new_target){
                    b_sum -= vb[bs];
                    bs++;
                }else if(b_sum < new_target){
                    if(be < m-1){
                        b_sum += vb[be + 1];
                    }
                    be++;
                }else{
                    printf("done\n");
                    ans++;
                    b_sum -= vb[bs];
                    bs++;
                }

                if(bs > be){
                    if(be < m-1){
                        b_sum += vb[be + 1];
                    }
                    be++;
                }
            }
        }
        
        // ****** end vb
        if(a_sum > target){
            a_sum -= va[as];
            as++;
        }else if(a_sum < target){
            if(ae < n-1){
                a_sum += va[ae + 1];
            }
            ae++;
        }else{
            // b 배열 조합 없음
            a_sum -= va[as];
            as++;
        }

        if(as > ae){
            if(ae < n-1){
                a_sum += va[ae + 1];
            }
            ae++;
        }

    }

	printf("%d", ans);
	return 0;
}