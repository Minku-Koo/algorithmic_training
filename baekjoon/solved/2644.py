"""
Date : 21.10.17
Problems : https://www.acmicpc.net/problem/2644
Title : 촌수 계산
"""
# BFS

# 촌수 딕셔너리 생성

def solution( p1, p2, fam ):
    parent = [p1,p2]
    def getParent(node):
        for i in fam.keys():
            if node in fam[i]:
                return i
        return -1
    
    while True:
        tmp  = getParent(parent[0])
        if tmp==-1: break
        else: parent[0] = tmp
        
    while True:
        tmp  = getParent(parent[1])
        if tmp==-1: break
        else: parent[1] = tmp
        

    if parent[0]!=parent[1]: return -1

    def bfs(fam, p, c):
        q = [p]
        visit = [[]]*101
        
        while q:
            node = q.pop(0)
            if node==c: return visit[node]
            if node not in fam.keys(): continue
            for j in fam[node]:
                
                if not visit[j]:
                    visit[j] = visit[node] + [j]
                    q.append(j)

        return 

    root1 = bfs(fam, parent[0], p1)
    
    root2 = bfs(fam, parent[1], p2)
    
    return len(set(root1)-set(root2)) + len(set(root2)-set(root1))


if __name__ == "__main__":
    n=int(input())
    p1, p2 = list(map(int, input().split()))
    row = int(input())
    fam = {}

    for i in range(row):
        p, c = list(map(int, input().split()))

        if p in fam.keys() :
            fam[p].append(c)
        else: fam[p] = [c]


    print(solution( p1, p2, fam ))

