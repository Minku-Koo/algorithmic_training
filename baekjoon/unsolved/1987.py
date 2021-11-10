"""
Date : 21.10.09
Problems : https://www.acmicpc.net/problem/1987
Title : 알파벳
"""
# BFS

def solution(height, width, graph):
    loc = (0,0)
    maxl = [0]
    box = graph[:]
    dy, dx = [-1,1,0,0], [0,0,1,-1]
    
    def bfs():
        result = 0
        #start = (0,0)
        dy, dx = [-1,1,0,0], [0,0,1,-1]
        q = [ (0,0, [], box[0][0]) ]
        check = []
        while q:
            y, x, check, visit = q.pop(0)
            #check.append((y,x))
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                # print(visit)
                if 0<=ny<height and 0<=nx<width :
                    if (ny, nx) not in check and box[ny][nx] not in visit:
                        nextLevel = visit+box[ny][nx]
                        nextCheck = check + [(ny, nx)]
                        q.append((ny, nx, nextCheck, nextLevel))
                        result = max(len(nextLevel), result)
            if result==26: return result

        return result


    return bfs()
    


if __name__ == "__main__":
    r, c = list(map(int, input().split()))
    box = []
    for _ in range(r):
        box.append( [j for j in input()] )

    result = solution(r, c, box)
    print(result)