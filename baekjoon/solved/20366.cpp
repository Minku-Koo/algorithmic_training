#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define MM 601

int v[MM] = {0};
int n;
int ans = 1000000001;

int checkAns(int snowman, int a, int b){
	int s = 0, e = n-1, res = 1000000001, snow2=0;
	while(s<e){
		if(s == a || s == b){
			s++;
			continue;
		}
		if(e == b || e == a){
			e--;
			continue;
		}
		
		int t = v[s] + v[e];
		
		if(t < snowman){
			s++;
		}
		else if(t > snowman){
			e--;
		}else{
			snow2 = t;
			break;
		}
		
		if(res >= abs(snowman - t)){
			res = abs(snowman - t);
			snow2 = t;
		}
	}
	return snow2;
}

int sol(){
	sort(v, v+n);
	
	int snowman1;
	for(int i=0; i<n; i++){
		for(int j=i+1;j<n; j++){
			snowman1 = v[i] + v[j];
			int snowman2 = checkAns(snowman1, i, j);
			ans = min(ans, abs(snowman1 - snowman2));
			if(ans == 0)
				return 0;
		}
	}
	
	return ans;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int t;
	
	cin >> n;
	for(int i=0; i<n; i++){
		cin >> t;
		v[i] = t;
	}
	
	printf("%d", sol());
	return 0;
}