

def solution(node, edge, graph):
    grp = {}
    for i in range(edge*2-1):
        if i%2==0:
            if grp.get(graph[i]): grp[graph[i]].append(graph[i+1])
            else :  grp[graph[i]] = [graph[i+1]]
            
    done = [] # 이미 마친 일 노드
    # print(grp)
    def func(node):
        if node in done: return
        for node_ in grp.get(node, []):
            func(node_)
        # print(node, end=' ')
        done.append(node)
    
    for j in range(1, node+1):
        func(j)
        
    return done[::-1]


T = 10
for tc in range(1,T+1):
    node, edge = list(map(int,input().split()))
    graph = list(map(int,input().split()))
    print(f"#{tc}", end=' ')
    r = solution(node, edge, graph)
    for j in r: print(j, end=' ')
    print()



 
