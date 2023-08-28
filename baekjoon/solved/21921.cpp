#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

struct node{
	int value; int count;
};

node sol(vector<int> &v, int x, int ival){
	int start = 0, end = x -1;
	node n = {ival, 1};
	int nsum = ival;
	int vlen = v.size();
	
	while(true){
		if(end >= vlen -1){
			break;
		}
		
		nsum = nsum - v[start] + v[end + 1];
		
		if(nsum > n.value){
			n.value = nsum;
			n.count = 1;
		}
		else if(nsum == n.value){
			n.count++;
		}
		
		start++; end++;
	}
	
	return n;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	node ans;
	int n, x, t;
	vector<int> v;
	cin >> n >> x;
	
	for(int i=0; i<n; i++){
		cin >> t;
		v.push_back(t);
	}
	
	//초기값
	int init_val = 0;
	for(int i=0; i<x; i++){
		init_val += v[i];
	}
	
	ans = sol(v, x, init_val);
	if(ans.value > 0)
	{
		printf("%d\n", ans.value);
		printf("%d", ans.count);
	}
	else{
		printf("SAD");
	}
	
	return 0;
}

