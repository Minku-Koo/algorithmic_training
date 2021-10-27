"""
Date : 21.10.15
Problems : https://www.acmicpc.net/problem/2468
Title : 안전 영역
"""

# BFS


def solution(size, land):
    maxVal = max([max(k) for k in land])
    water = 0


    def bfs(size, land, water):
        box = [j[:] for j in land]
        result = 0

        dy, dx = [1,-1,0,0], [0,0,-1,1]

        for y in range(size):
            for x in range(size):
                if 111>box[y][x] > water : #시작지점
                    result += 1
                    q = [(y, x)]
                    while q:
                        y_, x_ = q.pop(0)
                        for i in range(4):
                            ny, nx = y_+dy[i], x_+dx[i]
                            if 0<=ny<size and 0<=nx<size :
                                if water<box[ny][nx]<111 :
                                    q.append((ny, nx))
                                    box[ny][nx] = 111

                pass
        return result
    
    max_ = 0
    while water<=maxVal:
        result = bfs(size, land, water)
        if result>max_: max_ = result
        if result==0: break
        water+=1

    return max_


if __name__ == "__main__":
    size = int(input())
    land = []
    for _ in range(size):
        land.append( list(map(int, input().split())) )
    
    print(solution(size, land))








