#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define MM 200001
// 1,000,000,000

int n, c;
long long MX = 1000000000;
long long v[MM] ={0};
long long s, e, mid;
long long maxv = 0, minv = MX;

int check_all_possible(int bet){
	// 간격 n으로 두고 공유기 설치가 모두 가능한가
	// bet은 최소거리
	int cnt = 1;
	int last_idx = 0;
	for(int i=0; i<n; i++){
		if(v[i] - v[last_idx] >= bet){
			//설치 가능
			cnt++;
			last_idx = i;
		}
	}
	return cnt;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	long long ans = 0, t;
	
	cin >> n >> c;
	
	for(int i=0; i<n; i++){
		cin >> t;
		v[i] = t;
		if(minv > t) minv = t;
		if(maxv < t) maxv = t;
	}
	
	sort(v, v+n);
	
	s = 1; e = maxv - minv;
	while(s<=e){
		mid = (s+e) / 2;
		if(check_all_possible(mid) >= c){
			ans = max(ans, mid);
			s = mid + 1;
		}else{
			e = mid - 1;
		}
		
	}
	
	printf("%lld", ans);
	return 0;
}