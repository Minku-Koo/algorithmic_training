"""
Date : 21.10.09
Problems : https://www.acmicpc.net/problem/1987
Title : 알파벳
"""
from collections import deque

def solution(height, width, box):
    loc = (0,0)
    maxl = [0]
    dy, dx = [-1,1,0,0], [0,0,1,-1]
    
    def dfs(line, visit=[], alpha=[]):
        # print(maxl[0])
        y, x = line[-1]
        visit.append((y, x))
        # result.append(line[:])
        
        # print("line", line)
        newline = []
        for i in range(4):
            y_, x_ = y+dy[i], x+dx[i]
            if 0<=y_<height and 0<=x_<width and (y_, x_) not in visit:
                if box[y_][x_] not in alpha:
                    newline.append((y_, x_))
                    #alpha.append(graph[y_][x_])

                    j = (y_, x_)
                    line.append(j)
                    alpha.append(box[j[0]][j[1]])
                    dfs(line, visit, alpha)
                    line.pop()
                    alpha.pop()
                    visit.pop()

        # print("new", newline)
        # print("visit", visit)
        if not newline:
            if maxl[0] < len(line):
                maxl[0] = len(line)
            # result.append(line[:])
            return 
        # else:
        #     for j in newline:
        #         line.append(j)
        #         alpha.append(box[j[0]][j[1]])
        #         dfs(line, visit, alpha)
        #         line.pop()
        #         alpha.pop()
        #         visit.pop()
            
        return 



    dfs( deque([loc]), [], [])
    # print(result)
    return maxl[0]
    # maxv = 0
    # for r in result:
    #     if maxv < len(r):
    #         maxv = len(r)

    # return maxv


if __name__ == "__main__":
    r, c = list(map(int, input().split()))
    box = []
    for _ in range(r):
        box.append( [j for j in input()] )

    result = solution(r, c, box)
    print(result)