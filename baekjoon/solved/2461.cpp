#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define MM 1001

int MX = 1000000000;
int v[MM][MM] = {0,};
int idx[MM] = {0,};  // 현재 인덱스

int sol(int n, int m){
	int minv = MX, maxv = 0;
	int gap = 0, minidx = 0, mingap = MX;
	
	// 오림차순 정렬
	for(int i=0; i<n; i++)
		sort(v[i], v[i]+m);
	
	while(true){
		// 초기화
		minv = MX, maxv = 0;
		// min max 갱신
		for(int j=0; j<n; j++){
			int temp = v[j][idx[j]];
			if(temp > maxv){
				maxv = temp;
			}
			if(temp < minv){
				minv = temp;
				minidx = j;
			}
		}
		
		
		gap = maxv - minv;
		if(gap < mingap){
			mingap = gap;
		}
		
		// minidx 증가
		idx[minidx] += 1;
		// 끝에 닿으면 종료
		if (idx[minidx] == m)
			break;
	}
	
	return mingap;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, n, m, a;
	
	cin >> n >> m;
	for(register int i=0; i<n; i++){
		for(register int j=0; j<m; j++){
			cin >> a;
			v[i][j] = a;
		}
	}
	
	printf("%d", sol(n, m));
	return 0;
}