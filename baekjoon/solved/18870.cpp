#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;

#define MM 1000001

unordered_map<long long int, int> mm;

long long v[MM] = {0};
long long vs[MM] = {0};
int n;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, t;
	
	cin >> n;
	for(int i=0; i<n; i++){
		cin >> t;
		v[i] = t;
		vs[i] = t;
	}
	
	// sort
	sort(vs, vs+n);
	int s = 0;
	for(int i=0; i<n; i++){
		long long num = vs[i];
		if (mm.find(num) == mm.end()){
			mm[num] = s++;
		}
	}
	
	for(int i=0; i<n; i++)
		printf("%d ", mm[v[i]]);

	return 0;
}