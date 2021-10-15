"""
Date : 21.10.14
Problems : https://www.acmicpc.net/problem/5014
Title : 스타트링크
"""
# BFS
from collections import deque
def solution(F, S, G, U, D ):
    if S==G : return 0
    # S -> G

    q = deque([S])
    visit = [0] * (F+1)
    visit[S] = 1

    while q:
        floor = q.popleft()

        for i in  [U, -1*D]:
            newFloor = floor + i
            if 1<=newFloor<=F and visit[newFloor]==0:
                visit[newFloor] = visit[floor]+1
                q.append(newFloor)

                if newFloor == G: return visit[newFloor] -1

    return "use the stairs"


if __name__ =="__main__":
    F, S, G, U, D = list(map(int, input().split()))
    print(solution(F, S, G, U, D ))