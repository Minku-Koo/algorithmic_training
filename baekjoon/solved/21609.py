"""
Date : 21.10.22
Problems : https://www.acmicpc.net/problem/21609
Title : 상어 중학교
"""
# BFS
from collections import deque
def solution(n, m, box):
    score = 0
    def rotation(box):
        newbox = []
        length = len(box)
        for x in range(length ):
            nx = length - x - 1
            temp = []
            for y in range(length ):
                #ny = length - y -1
                temp.append( box[y][nx] )
            newbox.append(temp)
        return newbox

    def downFunc(line):
        result = []
        

        linesplit, temp = [], []
        for i in range(len(line)):
            if line[i]==-1: 
                if temp: linesplit.append(temp)
                temp = []
                linesplit.append([-1])
            else:
                temp.append(line[i])

        if temp: linesplit.append(temp)
        
        for row in linesplit:
            if len(row)>1 and row.count("#")>0:
                row_len = len(row)
                while row.count("#")>0:
                    row.remove("#")
                while len(row)<row_len:
                    row.append("#")
            result.extend(row)


        return result
    
    def goDown(box):
        length = len(box)
        
        for x in range(length):
            temp = []
            for y in range(length):
                ny = length - y  - 1
                temp.append(box[ny][x])
            for j, node in enumerate( downFunc(temp)):
                box[length-j-1][x] = node
                
        return box
                

    def bfs(node, box, rem=False):
        q = deque([node])
        color = box[node[0]][node[1]]
        visit = {node:True}
        if rem: box[node[0]][node[1]]="#"
        cnt=1
        rainbow=0
        dy, dx = [0,0,1,-1], [-1,1,0,0]
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny, nx  = y+dy[i], x+dx[i]
                if visit.get((ny, nx))!=None: continue
                if 0<=nx<n and 0<=ny<n:
                    
                    if box[ny][nx]==0 or box[ny][nx]==color :
                        if rem: box[ny][nx]="#"
                        if box[ny][nx]==0:
                            rainbow+=1
                        q.append((ny, nx))
                        visit[(ny, nx)] = True
                        cnt+=1
        return cnt, visit, box, rainbow

    
    while True:
        pos = {}
        loc = {}
        visited = {}
        for y in range(n):
            for x in range(n):
                if visited.get(box[y][x]) and (y,x) in visited[box[y][x]]: continue
                if str(box[y][x]).isdigit() and box[y][x]>0:
                    cnt, visit, _, rainbow = bfs( (y, x), box)
                    if cnt<2: continue
                    if visited.get(box[y][x]):
                        visited[box[y][x] ] |=  set(visit.keys())
                    else:
                        visited[box[y][x]] = visit.keys()
                    
                    if not pos.get( cnt ):
                        pos[cnt] = [(y, x, rainbow)]
                    else:
                        pos[cnt].append((y, x, rainbow))
                    loc[(y, x)] = visit
        if not pos: break
        
        maxKey = max(pos.keys())
        if len(pos[maxKey])>1:
            y, x,_ = sorted( pos[maxKey], key= lambda x:(x[-1],x[0],x[1]) )[-1]
            
        else:
            y, x, _ = pos[maxKey][0]
        score += maxKey**2
        _, _, box, _ = bfs( (y,x) , box, True)
        
        box = goDown(box)
        box = rotation(box)
        box = goDown(box)

    return score


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    box = []
    for i in range(n):
        box.append( list(map(int, input().split())) )
    
    print( solution(n, m, box)  )



