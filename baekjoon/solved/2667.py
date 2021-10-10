"""
Date : 21.10.09
Problems : https://www.acmicpc.net/problem/2667
Title : 단지번호붙이기
"""
from collections import deque


def solution(side, box):
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    ky = 1
    result = {}
    for y in range(side):
        for x in range(side):
            if box[y][x]==0: continue

            queue = deque([(y, x)])
            visit=[]
            while queue:
                p, q = queue.popleft()
                box[p][q] = 0
                if (p, q) not in visit:
                    visit.append( (p, q) )
                        
                    for i in range(4):
                        y_, x_ = p+dy[i], q+dx[i]
                        if 0<=y_<side and 0<=x_<side and box[y_][x_]!=0:
                            queue.append( (y_, x_) )

            result[ky] = len(visit)
            ky+=1
    
    print(len(result))
    return result

if __name__ =="__main__":
    side = int(input())
    box = [ list(map(int, [j for j in input()])) for _ in range(side)]
    
    result = solution(side, box)
    sresult = [result[i] for i in result]
    for r in sorted(sresult): print(r)
    pass


