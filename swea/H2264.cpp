// SWEA

#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>

extern void init(int N);
extern int arrive(int mId);
extern int leave(int mId);

/////////////////////////////////////////////////////////////////////////

#define CMD_INIT 1
#define CMD_ARRIVE 2
#define CMD_LEAVE 3

static bool run() {
	int q;
	scanf("%d", &q);

	int n, mid;
	int cmd, ans, ret = 0;
	bool okay = false;

	for (int i = 0; i < q; ++i) {
		scanf("%d", &cmd);
		switch (cmd) {
			case CMD_INIT:
				scanf("%d", &n);
				init(n);
				okay = true;
				break;
			case CMD_ARRIVE:
				scanf("%d %d", &mid, &ans);
				ret = arrive(mid);
				if (ans != ret)
					okay = false;
				break;
			case CMD_LEAVE:
				scanf("%d %d", &mid, &ans);
				ret = leave(mid);
				if (ans != ret)
					okay = false;
				break;
			default:
				okay = false;
				break;
		}
	}
	return okay;
}

int main() {
	setbuf(stdout, NULL);
	//freopen("sample_input.txt", "r", stdin);

	int T, MARK;
	scanf("%d %d", &T, &MARK);

	for (int tc = 1; tc <= T; tc++) {
		int score = run() ? MARK : 0;
		printf("#%d %d\n", tc, score);
	}

	return 0;
}

/*********************************************************/
/*********************************************************/
/*********************************************************/
/*********************************************************/

#include <iostream>
#include <set>
#include <unordered_map>
using namespace std;

struct Node{ // 빈 사물함 시작과 끝
	int start, end;
};
 

struct comp{ // 거리순, 아이디순 정렬
	bool operator()(const Node &a, const Node &b)const{
		int d1 = a.end - a.start + 1;
        int d2 = b.end - b.start + 1;
		if(d1 != d2)
			return d1 > d2;
		return a.start < b.start;
	}
};

unordered_map<int, int> id2locker; // id : 사물함 위치
set<Node, comp> emptyLocker; // 빈 사물함 거리
set<int> usingLocker; // 사용 중 사물함
 
int lSize;

void init(int N) {
	lSize = N;
	id2locker.clear();
	emptyLocker.clear();
	usingLocker.clear();
	
	// 양 옆 막아버리기
	emptyLocker.insert({ 0, lSize + 1 });
    usingLocker.insert(0);
    usingLocker.insert(lSize + 1);
	return;
}

int arrive(int mId) {
	auto dist = emptyLocker.begin();
	int start = dist->start;
	int end = dist->end;
	int loc = (start + end) / 2;
	
	if(start == 0) loc = 1;
	else if(end == lSize + 1) loc = lSize;
	
	emptyLocker.erase({start, end});
	emptyLocker.insert({start, loc});
	emptyLocker.insert({loc, end});
	
	id2locker[mId] = loc;
	usingLocker.insert(loc);
	
	int ans = loc;
	// printf("arrive: %d\n", ans);
	
	return ans;
}

int leave(int mId) {
	int loc = id2locker[mId];
	
	auto before = usingLocker.lower_bound(loc);
	auto after = usingLocker.upper_bound(loc);
	
	auto start = *(--before);
	auto end = *after;
	
	emptyLocker.erase({start, loc});
	emptyLocker.erase({loc, end});
	emptyLocker.insert({start, end});
	
	usingLocker.erase(loc);
	id2locker.erase(mId);
	
	int ans = lSize - id2locker.size();
	// printf("leave: %d\n", ans);
	
	return ans;
}
