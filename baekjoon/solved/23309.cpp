// https://www.acmicpc.net/problem/23309
// clear

#include <stdio.h>
#include <string>
#include <vector>
#include <iostream>

#define MM 1000001

using namespace std;

int stationCount, fixCount;

/*
BN i j : i 다음 역 출력하고 그 사이에 j 생성
BP i j : i 이전 역 출력하고 그 사이에 j 생성
CN i : i 다음 역 출력하고 폐쇄
CP i : i 이전 역 출력하고 폐쇄
*/

struct Node {
	int  p = 0, n = 0;
};

// 가능한 모든 역 고유 번호 배열
Node station[MM];
// 최초 입력 값을 받고, 링크드리스트 구현을 위한 vector
vector<int> first;

// insert next station
int insertNext(int from, int to) {
	int nextNum = station[from].n;

	if (nextNum == 0) { // if, start one station
		// 기존 역과 새로운 역 2개 연결
		Node t = { from, from };

		station[from].n = to;
		station[from].p = to;

		station[to] = t;
		return from;
	}

	Node t = { from, nextNum };

	station[from].n = to;
	station[nextNum].p = to;

	station[to] = t;
	return nextNum;
}

// insert prev station
int insertPrev(int from, int to) {
	int prevNum = station[from].p;

	if (prevNum == 0) { // if, start one station
		// 기존 역과 새로운 역 2개 연결
		Node t = { from, from };

		station[from].n = to;
		station[from].p = to;

		station[to] = t;
		return from;
	}

	Node t = { prevNum, from };

	station[from].p = to;
	station[prevNum].n = to;

	station[to] = t;
	return prevNum;
}

// remove next station
int remNext(int n) {
	int nextNum = station[n].n;
	int nnextNum = station[nextNum].n;

	station[n].n = nnextNum;
	station[nnextNum].p = n;

	station[nextNum] = {};
	return nextNum;
}

// remove prev station
int remPrev(int n) {
	int prevNum = station[n].p;
	int pprevNum = station[prevNum].p;

	station[n].p = pprevNum;
	station[pprevNum].n = n;

	station[prevNum] = {};
	return prevNum;
}


int main() {
	int  n;
	
	// ** 이 코드 없으면 시간초과 뜸 ******
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	// ******************************

	cin >> stationCount >> fixCount;
	
	// 시작 역이 하나인 경우
	if (stationCount == 1) {
		cin >> n;
		Node t = {};
		station[n] = t;
	}
	else { // 시작 역이 2개 이상인 경우
		for (register int i = 0; i < stationCount; ++i) {
			cin >> n;
			Node t = {};
			first.push_back((int)n);

			if (i < stationCount - 1) {
				// 이전 역 연결
				t.p = first[i - 1];
				// 이전 역의 다음 역 연결
				station[first[i - 1]].n = first[i];
			}
			else { // last node
				t.p = first[i - 1];
				station[first[i - 1]].n = first[i];
				t.n = first[0]; // next -> first station
				// first station prev -> last station
				station[first[0]].p = first[stationCount - 1];
			}
			station[first[i]] = t;
		}
	}

	string cmd;
	int from, to, ans;
	for (register int i = 0; i < fixCount; ++i) {
		cin >> cmd >> from;
		// 명령어 -> 해당 함수 실행
		if (cmd[0] == 'B') {
			cin >> to;
			if (cmd[1] == 'N')
				ans = insertNext(from, to);
			else
				ans = insertPrev(from, to);
		}
		else {
			if (cmd[1] == 'N')
				ans = remNext(from);
			else
				ans = remPrev(from);
		}
		
		printf("%d\n", ans);
	}

	return 0;
}