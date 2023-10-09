#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>

using namespace std;

#define MM 1001

long long target;
int n, m;
long long va[MM], vb[MM];
vector<long long> a_sum, b_sum;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	long long ans = 0;
	int t;
	
    cin >> target;
	cin >> n;
    for(int i=0; i<n; i++){
        cin >> t;
        va[i] = t;
    }
    
	cin >> m;
    for(int i=0; i<m; i++){
        cin >> t;
        vb[i] = t;
    }
    
    // solve
	long long sum_temp;
	// sliding window
	for(int window = 1; window <= n; window++){
		sum_temp=0;
		for(int i = 0; i<window; i++){
			sum_temp += va[i];
		}
		a_sum.push_back(sum_temp);
		for(int w_start = 0; w_start < n - window; w_start++){
			// sum_temp update
			sum_temp -= va[w_start];
			sum_temp += va[w_start + window];
			
			a_sum.push_back(sum_temp);
		}
	}
	
	for(int window = 1; window <= m; window++){
		sum_temp=0;
		for(int i = 0; i<window; i++){
			sum_temp += vb[i];
		}
		b_sum.push_back(sum_temp);
		for(int w_start = 0; w_start < m - window; w_start++){
			// sum_temp update
			sum_temp -= vb[w_start];
			sum_temp += vb[w_start + window];
			
			b_sum.push_back(sum_temp);
		}
	}
	
	vector<long long>::iterator itr;
	sort(b_sum.begin(), b_sum.end());
	
	// find
	int start, end;
	for(itr = a_sum.begin(); itr!=a_sum.end(); itr++){
		long long new_target = target - *itr;
		start = lower_bound(b_sum.begin(), b_sum.end(), new_target) - b_sum.begin();
		end = upper_bound(b_sum.begin(), b_sum.end(), new_target) - b_sum.begin();
		ans += (end - start);
	}


	printf("%lld", ans);
	return 0;
}