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
# Input : 루트 노드 값
def iterative_bfs(root):
    discovered = [root] # 탐색한 노드에 루트 노드 추가
    queue = [root] # 큐에 루트 노드 추가
    while queue: # 큐가 빌 때 까지 반복
        x = queue.pop(0) # 큐에서 꺼내옴
        
        for node in graph[x]: # 해당 노드의 모든 하위 노드
            if node not in discovered: # 탐색한 적이 없으면
                discovered.append(node) # 탐색한 노드에 추가
                queue.append(node) # 큐에 추가

    return discovered #탐색 결과

print( iterative_bfs(1) )