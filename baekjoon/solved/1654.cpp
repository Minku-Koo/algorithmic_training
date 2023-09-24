#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define MK 10000

long long v[MK + 1] = {0};
long long maxv_val = 0;
int k, n;

long long  checkCount(long long  m){
	long long  checksum = 0;
	for(int i=0; i<k; i++)
		checksum += (v[i] / m);
	return checksum;
}

long long sol(){
	long long ans = 0;
	// division by zero 방지 -> s = 0
	long long s = 1, m, e =maxv_val;
	m =e;
	
	while(e>=s){
		m = (s + e) / 2;
		int cnt = checkCount(m);
		if(cnt >= n){
			// 늘려도됨
			// 정답 갱신
			ans = max(ans, m);
			s = m + 1;
		}else{
			// 줄여야함
			e = m - 1;
		}
	}
	
	return ans;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	long long t;
	cin >> k >> n;
	for(int i=0; i<k; i++){
		cin >> t;
		if(maxv_val < t){
			maxv_val = t;
		}
		v[i] = t;
	}
	
	printf("%lld", sol());
	return 0;
}