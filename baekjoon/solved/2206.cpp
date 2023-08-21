// https://www.acmicpc.net/problem/2206
// unclear

#include <iostream>
#include <stdio.h>
#include <unordered_map>
#include <vector>
#include <queue>
#include <string.h>

#define ML 1001

using namespace std;


struct Cell{
	int y, x, num, count = 1, broken = 0;
};

int nn, mm, n;
int minCount = ML * ML;
Cell box[ML][ML];
bool visit[ML][ML];

int dy[4] = {0,0,1,-1};
int dx[4] = {-1,1,0,0};

int solve(){
	queue<Cell> qq;
	
	qq.push(box[0][0]);
	visit[0][0] =  true;
	
	while(!qq.empty()){
		
		Cell now = qq.front();
		qq.pop();
		
		for(int i = 0; i < 4; i++){
			int ny = now.y + dy[i];
			int nx = now.x + dx[i];
			
			
			// 박스 밖인 경우 continue
			if(ny >= nn || nx >= mm || ny < 0 || nx < 0){
				continue;
			}
			
			if(visit[ny][nx]){
				continue;
			}
			
			// now.broken이 1 && next num == 1 -> continue
			if(now.broken == 1 && box[ny][nx].num == 1){
				continue;
			}
			
			// minCount보다 크거나 같은 경우 continue
			if(minCount <= now.count + 1){
				continue;
			}
			
			int bk = 0; // 벽일 경우 broken + 1
			if(box[ny][nx].num == 1)
				bk = 1;
			
			
			// count calc
			if(ny == nn - 1 && nx == mm -1){
				if(now.count + 1 < minCount){
					minCount = now.count + 1;
					printf("find: [%d %d] num %d count %d brk %d\n", ny, nx, box[ny][nx].num, minCount, bk);
				}
			}
			else{
				// 그 외 queue input
				box[ny][nx].count = now.count + 1;
				box[ny][nx].broken = now.broken + bk;
				qq.push(box[ny][nx]);
				visit[ny][nx] =  true;
				printf("search: [%d %d] num %d count %d brk %d\n", ny, nx, box[ny][nx].num, box[ny][nx].count, box[ny][nx].broken);
			}
		}
		
		
	}
	
	if(minCount == ML * ML){
		minCount = -1;
	}
	
	return minCount;
}

int main(){
	cin >> nn >> mm;
	memset(visit, 0, sizeof(visit));
	for(int i = 0; i<nn; i++){
		char k[ML];
		scanf("%s", k);
		for(int j = 0; j<mm; j++){
			Cell c = {i, j, k[j] - '0', 1, 0};
			box[i][j] = c;
		}
	}
	
	int ans = solve();
	cout << ans;
	
	return 0;
}

