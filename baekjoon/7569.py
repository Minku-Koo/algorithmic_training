"""
Date : 21.10.08
Problems : https://www.acmicpc.net/problem/7569
Title : 토마토
"""
from collections import deque

# BFS
class Tomato:
    def __init__(self, M, N, H, box):
        self.width = M
        self.height = N
        self.floor = H

        self.box = []
        for i in range(N*H):
            if i%N ==0:
                self.box.append( box[i:i+N] )
        
        self.tomato = []
        self.isZero = self.getTomato()
        
    def solution(self):
        # 모두 익었는지 확인 > 익었다면 0 반환
        if not self.isZero: return 0

        self.bfs()

        result = 0
        for floor in self.box:
            for b in floor:
                if 0 in b: return -1
                maxv = max(b)
                if result < maxv: result = maxv

        return result-1


    def bfs(self):
        queue = deque(self.tomato[:])
        dh = [-1,1,0,0,0,0]
        dy = [0,0,1,-1,0,0]
        dx = [0,0,0,0,1,-1]

        while queue:
            h, y, x = queue.popleft()
            for i in range(6):
                h_, y_, x_ = h + dh[i], y+dy[i], x+dx[i]
                if 0<=h_<self.floor and 0<=y_<self.height and 0<=x_<self.width:
                    if self.box[h_][y_][x_] == 0 :
                        queue.append( (h_, y_, x_) )
                        self.box[h_][y_][x_] = self.box[h][y][x]+1

        
    def getTomato(self):
        isZero = False
        for h, floor in enumerate(self.box):
            for y, line in enumerate(floor):
                for x, t in enumerate(line):
                    if t == 0: isZero=True
                    if t==1:
                        self.tomato.append((h, y, x))

        return isZero

    
if __name__ == "__main__":
    M, N, H = list(map(int, input().split()))
    box = []
    for _ in range(N*H):
        box.append( list(map(int, input().split())) )

    tomato = Tomato(M,N,H, box)
    print(tomato.solution())
    pass

