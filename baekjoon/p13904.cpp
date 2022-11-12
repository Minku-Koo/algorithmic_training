//

#include <stdio.h>

#define MD 1001
#define MW 101

using namespace std;

int arr[MD][MW] = {0,};

int solve(int day){
	int ans = 0;
	
	// 가장 큰 날부터 반복
	while(day>0){	
		// 해당 날에서 가장 큰 일 정답에 플러스
		int maxw = 0, mx = 0;
		for(int j=1; j<=arr[day][0]; j++){
			if(maxw < arr[day][j]){
				maxw = arr[day][j];
				mx = j;
			}
		}
		ans += maxw;
		// 남은 일은 -1 날짜에 추가
		for(int j=1; j<=arr[day][0]; j++){
			if(j==mx) continue;
			arr[day-1][++arr[day-1][0]] = arr[day][j];
		}
		day--;
	}
	return ans;
}

int main(){
	
	int n,d,w, maxd = 1;
	
	scanf("%d", &n);
	
	for(int j=0; j<n; ++j){
		
		scanf("%d %d", &d, &w);
		arr[d][ ++arr[d][0] ] = w;
		
		if(maxd < d) maxd = d;
	}
	
	int r = solve(maxd);
	printf("%d\n", r);
	
	return 0;
}