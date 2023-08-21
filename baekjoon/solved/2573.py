"""
Date : 21.10.08
Problems : https://www.acmicpc.net/problem/2573
Title : 빙산
"""
from collections import deque

# BFS

class Ice:
    def __init__(self, M, N, block):
        self.width = N
        self.height = M
        self.block = block
        self.loc = []

        self.setIceLoc()
        # print(self.loc)

    def solution(self):
        result = 0
        while True:
            if sum([sum(k) for k in self.block])==0:
                return 0
            self.melting()
            
            r = self.checkBlock()
            result+=1
            if r >1 : 
                return result
        

    def setIceLoc(self):
        for y, line in enumerate(self.block):
            #if y==0 or y==self.height-1: continue
            for x, ice in enumerate(line):
                #if x==0 or x==self.width-1: continue
                if ice >0: self.loc.append((y,x))

    def checkMelt(self, loc):
        y, x = loc
        dy = [0,0,1,-1]
        dx = [-1,1,0,0]
        melt = 0
        for j in range(4):
            y_, x_ = y+dy[j], x+dx[j]
            if self.block[y_][x_]==0:
                melt += 1

        return melt

    def melting(self):
        empty = []
        for _ in range(self.height):
            empty.append([-1]*self.width)
        
        rm_ice = []
        for ice in self.loc:
            y, x  = ice
            empty[y][x] = max(0, self.block[y][x] - self.checkMelt((y, x)) )
            if empty[y][x]==0:
                rm_ice.append(ice)

        for j in rm_ice:
            self.loc.remove(j)
        
        for ice in self.loc:
            i, j = ice
            self.block[i][j] = empty[i][j]
            #print(">",ice)
        #print("--")
        # for i, q in enumerate(empty):
        #     for j, t in enumerate(q):
        #         if t!=-1:
        #             self.block[i][j] = t


    def checkBlock(self):
        
        block = 0
        visit = []
        iterloc = self.loc[:]
        for l in iterloc:
            y, x = l
            if (y, x) in visit: continue
            q = deque([(y, x)])
            while q:
                ny, nx = q.popleft()

                if (ny, nx) not in visit:
                    visit.append( (ny, nx) ) 
                    dy = [0,0,1,-1] 
                    dx = [-1,1,0,0] 
                    
                    for j in range(4):
                        y_, x_ = ny+dy[j], nx+dx[j]
                        if (y_, x_) in iterloc:
                            q.append((y_, x_))

            block+=1



        # for y in range(self.height):
        #     if y==0 or y==self.height-1: continue
        #     for x in range(self.width):
        #         if x==0 or x==self.width-1: continue

        #         if self.block[y][x]>0:
        #             #if empty[y][x] != -1: continue
        #             q = deque([(y, x)])
        #             if (y, x) in visit: continue
        #             # print(">", y, x)
        #             while q:
        #                 ny, nx = q.popleft()

        #                 if (ny, nx) not in visit:
        #                     visit.append( (ny, nx) ) 
        #                     dy = [0,0,1,-1] 
        #                     dx = [-1,1,0,0] 
                            
        #                     for j in range(4):
        #                         y_, x_ = ny+dy[j], nx+dx[j]
        #                         if self.block[y_][x_]>0:
        #                             q.append((y_, x_))

        #             block+=1
        
        # print("block:", block)
        return block


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    block = []
    for _ in range(N):
        block.append(list(map(int, input().split())))

    ice = Ice(N, M, block)
    print(ice.solution())
    pass
