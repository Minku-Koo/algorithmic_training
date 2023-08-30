#include <stdio.h>
#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

#define MM 4000001

int v[MM] = {0,};
vector<int> arr;

void getsosu(int v[], int n){
	v[1] = 0;
	for(int i=2; i<(int)sqrt(n) + 1; i++){
		for(int j=i + i; j<=n; j += i)
			v[j] = 0;
	}
	
	for(int i=0; i<=n; i++){
		if(v[i] != 0){
			arr.push_back(v[i]);
		}
	}
	
	return;
}

int sumRange(int s, int e){
	int ans = 0;
	for(register int i=s; i<=e; i++){
		ans += arr[i];
	}
	return ans;
}

int sol(int n){
	int ans = 0;
	for(int i=0; i<=n; i++){
		v[i] = i;
	}
	getsosu(v, n);
	
	int start = 0, end=0, t;
	int vlen = arr.size() - 1;
	while(start <= vlen && end <= vlen){
		t = sumRange(start, end);
		if(t > n){
			start++;
		}else if(t == n){
			start++; end++; ans++;
		}else{
			end++;
		}
	}
	return ans;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, n;
	
	cin >> n;
	ans = sol(n);
	printf("%d", ans);
	return 0;
}