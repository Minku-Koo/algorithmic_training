#include <iostream>
// #include <queue>
using namespace std;
 
#define MAX 100001
 
int N, T;
int arr[MAX];
int carr[MAX];
// int result[MAX];
 
bool possible(int diff)
{
        for (int i = 0; i < N; i++)
                 carr[i] = arr[i];
 
        int cnt = 0;
        //인접한 오른쪽 체크
        for (int i = 0; i<N - 1; i++)
                 if (carr[i + 1] - carr[i] > diff)
                 {
                         cnt += carr[i + 1] - (carr[i] + diff);
                         carr[i + 1] = carr[i] + diff;
                 }
        //인접한 왼쪽 체크
        for (int i = N - 1; i > 0; i--)
                 if (carr[i - 1] - carr[i] > diff)
                 {
                         cnt += carr[i - 1] - (carr[i] + diff);
                         carr[i - 1] = carr[i] + diff;
                 }
 
        //변경 횟수가 T 이하인가 체크
        if (cnt <= T)
                 return true;
        return false;
}
 
int main(void)
{
        // ios_base::sync_with_stdio(0);
		int test_case;
		int tc;
		
		
		cin>>tc;
        // cin.tie(0);
		for(test_case = 1; test_case <= tc; ++test_case)
		{
        cin >> N >> T;
 
        for (int i = 0; i < N; i++)
                 cin >> arr[i];
 
        int low = 0, high = 1e9;
        int minDiff = 1e9; //최소 차
		int result = 1;

        while (low <= high)
        {
                 int mid = (low + high) / 2;
                 if (possible(mid))
                 {
                         // for (int i = 0; i < N; i++)
                                 // result[i] = carr[i];
                         high = mid - 1;
						 result = mid;
                 }
                 else
                         low = mid + 1;
        }

        // for (int i = 0; i < N; i++)
                 // cout << result[i] << " ";
		cout << "#" << test_case<<" " << result ;
        cout << "\n";
		}
		
        return 0;
}

// #1 18
// #2 4
// #3 13
// #4 19
// #5 27
// #6 22
// #7 15
// #8 16
// #9 11
// #10 6
// #11 1877
// #12 4660
// #13 2822
// #14 5950
// #15 6282
// #16 6140
// #17 4895
// #18 3053
// #19 6322
// #20 6136

