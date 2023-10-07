#include <stdio.h>
#include <iostream>
#include <unordered_map>

using namespace std;

int n, m;
unordered_map<int, int> mm;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ans = 0, t;
	
	cin >> n;
    for(int i=0; i<n; i++){
        cin >> t;
        mm[t] += 1;
    }

    cin >> m;
    for(int i=0; i<m; i++){
        cin >> t;
        printf("%d ", mm[t]);
    }

	return 0;
}