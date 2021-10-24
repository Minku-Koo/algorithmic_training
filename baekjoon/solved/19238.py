"""
Date : 21.10.22
Problems : https://www.acmicpc.net/problem/19238
Title : 스타트 택시
"""
# BFS
from collections import deque

def solution(n, m, oil, box, taxi, custom):
    customCoord = []
    taxi = [taxi[0]-1, taxi[1]-1]
    for i, line in enumerate(custom):
        custom[i] = [j-1 for j in line]
    # 벽 to -1
    for y in range(n):
        for x in range(n):
            if box[y][x]==1: box[y][x]=-1
            
    for i in range(m):
        customCoord.append( tuple(custom[i][:2]) )

    def bfs(taxi, oil, customCoord, box):
        
        nbox = [b[:] for b in box]
        result = {}
        ty, tx = taxi
        if tuple(taxi) in customCoord:
            
            result[0] = [customCoord.index(tuple(taxi))]
        
        
        q = deque([(ty, tx)])
        nbox[ty][tx]=1
        dy, dx = [0,0,-1,1], [1,-1,0,0]
        cnt = 0
        while q:
            y, x = q.popleft()
                    
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0<=ny<n and 0<=nx<n:
                    if nbox[ny][nx]!=-1 and nbox[ny][nx]==0:
                        q.append( (ny, nx) )
                        nbox[ny][nx] = nbox[y][x]+1
                    
                        if (ny, nx) in customCoord:
                            cnt+=1
                            
                            if result.get(nbox[y][x]):
                                result[nbox[y][x]].append( customCoord.index((ny, nx)) )
                            else:
                                result[nbox[y][x]] = [customCoord.index((ny, nx))]
            
            if cnt == len(customCoord):
                break
            
        return result, box

    def bfs_target(taxi, oil, target, box):
        ty, tx = taxi
        
        nbox = [b[:] for b in box]
        q = deque([(ty, tx)])
        nbox[ty][tx]=1
        dy, dx = [0,0,-1,1], [1,-1,0,0]

        while q:
            y, x = q.popleft()
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0<=ny<n and 0<=nx<n:
                    if nbox[ny][nx]!=-1 and nbox[ny][nx]==0:
                        q.append( (ny, nx) )
                        nbox[ny][nx] = nbox[y][x]+1
                        if (ny, nx) == target:
                            return nbox[y][x], box
            
        return -1, box


    while True:
        
        customs, box = bfs( taxi, oil, customCoord , box)
        
        if custom and not customs: return -1
        
        minDist = min(customs.keys())
        
        if len( customs.get(minDist))>1:
            c = sorted([customCoord[c] for c in customs[minDist]], key = lambda x:(x[0], x[1]) )[0]
            targetCustom =customCoord.index(c)
            pass
        else:
            targetCustom = customs.get(minDist)[0]
            
        customNow = tuple(custom[targetCustom][:2])
        target = tuple(custom[targetCustom][2:])
        
        custom.remove( custom[targetCustom] )
        customCoord.remove(customCoord[targetCustom] )

        oil -= minDist
        
        if oil<0: return -1
        taxi = [ customNow[0], customNow[1] ]
        
        targetDist, box = bfs_target(taxi, oil, target, box)
        if targetDist==-1: return -1
        
        oil -= targetDist
        if oil<0: return -1
        oil += targetDist*2

        taxi = [ target[0], target[1] ]
        
        if len(custom)==0: break
        
    return  oil


if __name__ == "__main__":
    n, m, oil = list(map(int, input().split()))
    box = []
    for _ in range(n):
        box.append( list(map(int, input().split())) )
    
    taxi = list(map(int, input().split()))

    custom = []
    for _ in range(m):
        custom.append( list(map(int, input().split())) )

    print( solution(n, m, oil,box, taxi, custom ) )
