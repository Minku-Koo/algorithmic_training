graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]
}

# BFS는 재귀 함수 사용 불가

# Queue를 이용한 BFS
def iterative_bfs(root):
    discovered = [root]
    queue = [root]
    while queue:
        x = queue.pop(0)
        
        for node in graph[x]:
            if node not in discovered:
                discovered.append(node)
                queue.append(node)

    return discovered

print( iterative_bfs(1) )