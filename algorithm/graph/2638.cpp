// https://www.acmicpc.net/problem/number
// clear

#include <iostream>
#include <stdio.h>
#include <queue>
#include <vector>
#include <string.h>

#define MM 101

using namespace std;

int N, M;
int box[MM][MM];
bool visited[MM][MM];
int checkEmpty = 0;

int dy[4] = {0,0,1,-1};
int dx[4] = {-1,1,0,0};

struct Node{
	int y, x, melt;
};


vector<Node> v; // cheese pos

bool check(){
	for(int i = 0; i < v.size(); i++)
		if(v[i].melt == false)
			return false;
	return true;
}

void fill(int y, int x){
	if(box[y][x] == 2) return;
	queue<Node> q;
	q.push({y, x, false});
	box[y][x] = 2;
	
	while(!q.empty()){
		Node now = q.front();
		q.pop();
		
		for(int i = 0; i<4; i++){
			int ny = now.y + dy[i];
			int nx = now.x + dx[i];
			
			if(ny >= N || nx >= M || nx < 0 || ny < 0)
				continue;
			if(box[ny][nx] != 0)
				continue;
			
			q.push({ny, nx, false});
			box[ny][nx] = 2;
			checkEmpty--;
		}
	}
}

void melt(){
	vector<Node> temp;
	// vector에서 좌표 받아오기
	for(int i = 0; i < v.size(); i++){
		Node n = v[i];
		// melt 확인
		if(n.melt) continue;
		// 접점 확인 
		int count = 0;
		for(int j = 0; j < 4; j++){
			int ny = n.y + dy[j], nx = n.x + dx[j];
			if(ny >= N || nx >= M || nx < 0 || ny < 0)
				continue;
			if(box[ny][nx] == 2) count++;
		}
		// if melt -> erase 갱신  melt vec 저장
		if(count >= 2){
			v[i].melt = true;
			temp.push_back({n.y, n.x, true});
		}
	}
	
	// melt vec -> box 2 치환
	for(int i = 0; i < temp.size(); i++){
		Node t = temp[i];
		// 녹은 위치에서 -> 주변 0 bfs로 채우기
		fill(t.y, t.x);
		box[t.y][t.x] = 2;
	}
}

int solve(){
	int result = 0;
	while(check() == false){
		melt();
		result++;
	}
	return result;
}

int main(){
	memset(box, 0, sizeof(box));
	memset(visited, 0, sizeof(visited));
	v.clear();
	cin >> N >> M;
	
	Node startPoint ;
	
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			cin >> box[i][j];
			if(box[i][j] == 0){}
			else{
				v.push_back({i, j, false});
			}
		}
	}
	
	// bfs 바같쪽 2로 치환
	queue<Node> q;
	q.push({0,0,false});
	visited[0][0] = true;
	box[0][0] = 2;
	
	while(!q.empty()){
		Node now = q.front();
		q.pop();
		
		for(int i = 0; i<4; i++){
			int ny = now.y + dy[i];
			int nx = now.x + dx[i];
			
			if(ny >= N || nx >= M || nx < 0 || ny < 0)
				continue;
			if(visited[ny][nx])
				continue;
			if(box[ny][nx] == 1)
				continue;
			
			q.push({ny, nx, false});
			box[ny][nx] = 2;
			visited[ny][nx] = true;
			
		}
	}
	
	
	
	int ans = solve();
	printf("%d", ans);
	
	return 0;
}

