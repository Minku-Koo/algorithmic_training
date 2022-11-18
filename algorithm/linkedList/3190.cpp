// https://www.acmicpc.net/problem/3190
// clear

#include <stdio.h>
#include <string>
#include <iostream>

#define MM 101

using namespace std;

int bSize, appleCount, turnCount;		// map size, apple count, turn count
bool appleBox[MM][MM];					// apple position
int turnSec[MM];						// turn sec
char turnDir[MM];						// turn direction
int turnOrderCount = 0;					// calc turn count

struct Node {
	int y = 0, x = 0;		// now position
	int ny = 0, nx = 0;		// next position
};

// map
Node snakeBox[MM][MM];
// head node, tail node
Node head, tail;

int dir = 0; // 0 오른쪽 1 왼쪽 2 위쪽 3 아래쪽
int ans = 0;

int dy[4] = { 0, 0, -1, 1 };
int dx[4] = { 1, -1, 0, 0 };

// 초기화
void init() {
	Node t;
	t.y = 1;
	t.x = 1;

	snakeBox[1][1] = t;
	// head == tail
	head = snakeBox[1][1];
	tail = snakeBox[1][1];
	return;
}



// 종료 조건 : 뱀 만나거나 or 벽 만나거나
bool isEnd(int y, int x) {
	if (y > bSize || x > bSize || y <= 0 || x <= 0) 
		return true;
	if (snakeBox[y][x].y != 0 && snakeBox[y][x].x != 0) 
		return true;
	return false;
}


// 이동 : 그냥 앞으로 -> 사과 만난지 확인 -> 늘리던가 꼬리자르던가
bool snakeMove() {
	int y, x, ny, nx;

	y = head.y;
	x = head.x;
	
	ny = y + dy[dir];
	nx = x + dx[dir];
	
	if (isEnd(ny, nx)) 
		return false;
	
	// head update 
	Node t = {ny, nx, 0, 0};
	snakeBox[ny][nx] = t;

	snakeBox[y][x].ny = ny;
	snakeBox[y][x].nx = nx;

	head = t;
	
	// 사과 만난건지? -> 만났다면 사과삭제 + 꼬리그대로 
	//					만나지 않았다면 -> 꼬리 자름
	if (appleBox[ny][nx]) {
		appleBox[ny][nx] = false;	// remove apple
		if(tail.ny == 0 && tail.nx == 0){ // if snake size is 1
			// tail next -> head
			tail.ny = ny;
			tail.nx = nx;
			snakeBox[tail.y][tail.x] = tail;
		}
	}
	else{
		// 사과 만나지 않음 -> 꼬리 자름
		int ty = tail.y, tx = tail.x; // tail position
		if(tail.ny == 0 && tail.nx == 0){
			// if snake size is 1 -> head == tail
			tail = snakeBox[head.y][head.x];
		}else{
			tail = snakeBox[tail.ny][tail.nx];
		}
		// remove tail
		snakeBox[ty][tx] = {0,0,0,0};
	}
	
	return true;
}

// t초 지났을 때, 방향 변경
void timeOrder() {
	if(turnOrderCount == turnCount) return;
	// after turn sec
	if (ans == turnSec[turnOrderCount]) {
		char d = turnDir[turnOrderCount];
		// 0 오른쪽 1 왼쪽 2 위쪽 3 아래쪽
		/*
			L
			0 : 2
			1 : 3
			2 : 1
			3 : 0
			D
			0 : 3
			1 : 2
			2 : 0
			3 : 1
		*/
		if (d == 'L') {
			if (dir == 0) dir = 2;
			else if (dir == 1)dir = 3;
			else if (dir == 2)dir = 1;
			else dir = 0;
		}
		else { // D
			if (dir == 0) dir = 3;
			else if (dir == 1)dir = 2;
			else if (dir == 2)dir = 0;
			else dir = 1;
		}
		turnOrderCount++;
	}
	return;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> bSize >> appleCount;
	for (int i = 0; i < appleCount; i++) {
		int y, x;
		cin >> y >> x;
		appleBox[y][x] = true;
	}

	cin >> turnCount;
	for (int i = 0; i < turnCount; i++){
		cin >> turnSec[i] >> turnDir[i];
	}

	init();
	
	while (true) {
		if (!snakeMove()) // finish
			break;
		
		ans++;
		timeOrder(); // turn sec -> turn direction
	}
	printf("%d\n", ++ans);
	return 0;
}
