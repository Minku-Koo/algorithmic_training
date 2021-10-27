"""
Date : 21.10.15
Problems : https://www.acmicpc.net/problem/2178
Title : 미로 탐색
"""
# BFS

def solution(height, width, box):
    
    q = [(0,0)]
    visit = []
    dy, dx = [0,0,1,-1], [-1,1,0,0]

    while q:
        y, x = q.pop(0)

        if y==height-1 and x==width-1:
            return box[y][x]

        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<height and 0<=nx<width:
                if (ny,nx) not in visit and box[ny][nx]>0:
                    q.append((ny, nx))
                    visit.append((ny, nx))
                    if box[ny][nx]==1:
                        box[ny][nx] = box[y][x]+1
                    else:
                        box[ny][nx] = min(box[ny][nx] ,box[y][x]+1)

        
    return

if __name__ == "__main__":
    n,m = list(map(int, input().split()))
    box = []
    for _ in range(n):
        box.append([int(j) for j in input()])

    print(solution(n,m,box))

