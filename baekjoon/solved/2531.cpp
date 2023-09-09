#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

#define MM 30001
#define MK 3001

int v[MM] = {0,};
int checked[MK] = {0,};
int s=0, e=0;

int sol(int n, int k, int d, int c){
	int ans, temp = 1;
	s = 0;
	e = k - 1;
	/*
	n 접시 수
	k 연속해서 먹어야되는 접시 수
	c 쿠폰번호
	d 초밥 가지수
	*/
	checked[c] = 1;
	for(int j = s; j <= e; j++){
		int i = j % n;
		if(checked[v[i]] == 0){
			temp++;
		}
		checked[v[i]] += 1;
	}
	
	ans =  temp;
	
	for(s = 0; s < n; s++){
		// 범위에 포함된 종류 개수와 k 포함여부 구하기
		checked[v[s]]--;
		if(checked[v[s]] == 0) temp--;
		if(checked[v[(e + 1) % n]] == 0) temp++;
		checked[v[(e + 1) % n]]++;
		
		ans = max(ans, temp);
		if(ans == d + 1){
			return ans;
		}
		e++;
	}
	
	
	return ans;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, n, k, c, d, ci;
	
	cin >> n >> d >> k >> c;
	
	for(int i =0; i<n; i++){
		cin >> ci;
		v[i] = ci;
	}
	
	printf("%d", sol(n, k, d, c));
	return 0;
}