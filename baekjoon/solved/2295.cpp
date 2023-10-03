#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define MM 1001

int ln;
long long t;
long long v[MM] = {0};


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
    // input
	cin >> ln;
	for(int i=0; i<ln; i++){
        cin >> t;
        v[i] = t;
    }
	
	vector<long long> checked(ln * ln);

    // solve
    sort(v, v+ln);
	
	int num= 0;
	// 두 수의 합
	for(int i=0; i<ln; i++){
		for(int j=0; j<ln; j++){
			checked[num++] = v[i] + v[j];
		}
	}
	
	sort(checked.begin(), checked.end());
	
	// 두 수의 합이 checked에 있는가?
	for(int i=ln-1; i>=0; i--){
		for(int j=i; j>=0; j--){
			long long target = v[i] - v[j];
			// target is in checked?
			int s = 0, m, e = checked.size() - 1;
			while(s<=e){
				m = (s + e) / 2;
				if(checked[m] < target){
					s = m + 1;
				}else if(checked[m] > target){
					e = m - 1;
				}else{
					printf("%lld", v[i]);
					return 0;
				}
			}
		}
	}

	return 0;
}