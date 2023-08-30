#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

#define MM 2000000001

void vsort(vector<int> &v){
	int temp, vlen = v.size();
	for(register int i=0; i<vlen; i++){
		for(register int j=i+1; j<vlen; j++){
			if(v[i] > v[j]){
				temp = v[i];
				v[i] = v[j];
				v[j] = temp;
			}
		}
	}
	return;
}

int sol(vector<int> &v, int m){
	int start =0, end=0, ans=MM, temp;
	int vlen = v.size();
	
	sort(v.begin(), v.end());
	while(start < vlen){
		temp = abs(v[end] - v[start]);
		if(temp == m){
			return temp;
		}
		
		if(temp > m){
			start++;
			if(temp < ans){
				ans = temp;
			}
			
		}else{
			// temp < m
			end++;
			if(end >= vlen){
				return ans;
			}
		}
	}
	return ans;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, a, b, t;
	vector<int> v;
	
	cin >> a >> b;
	for(register int i =0; i<a; i++){
		cin >>t;
		v.push_back(t);
	}
	
	ans = sol(v, b);
	
	printf("%d", ans);
	return 0;
}