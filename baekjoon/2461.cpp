#include <stdio.h>
#include <iostream>

using namespace std;

#define MM 1001

int v[MM][MM] = {0,};

int sol(int n, int m){
	int ans = 0;
	
	// 내림차순 정렬
	
	// [2] max min 차이 저장, 가장 큰 값의 인덱스 찾기
	
	// max값이 있는 인덱스 하나 줄여가면서 비교
	// 줄였더니 더 줄어들면, 반복 / 줄였더니 더 커지면 [2]로 돌아감
	
	return ans;
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