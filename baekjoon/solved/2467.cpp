#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define MX 100001
long long MM = 1000000001;


long long v[MX] = {0};
int n;

struct Node{
    long long a, b, sum;
};

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
    long long ans, t;
	
    // input
	cin >> n;
    for(int i=0; i<n; i++){
        cin >> t;
        v[i] = t;
    }
    
    // solve
    Node result;
    result.sum = MM * 2;
    for(int j=0; j<n-1; j++){
        long long start = v[j];
        long long temp;
        // 왼쪽부터 값 찾기
        int s=j, e=n-1, mid;
        while(s <= e){
            mid = (s + e) / 2;
            if(mid == j) {
                s = mid + 1;
                continue;
            }
            temp = start + v[mid];
            
            
            if(temp < 0){ // 증가시킴
                s = mid + 1;
            }else{ // 감소시킴
                e = mid -1;
            }

            if(temp < 0) temp *= -1;

            if(result.sum > temp){
                result.a = start;
                result.b = v[mid];
                result.sum = temp;
                if(temp == 0){
                    printf("%lld %lld", start, v[mid]);
                    return 0;
                }
            }
        }
        
    }

	printf("%lld %lld", result.a, result.b);
	return 0;
}