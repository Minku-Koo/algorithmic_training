graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]
}

# 재귀 함수 이용한 DFS
# Input : 루트 노드 값
def recursion_dfs(node, discovered=[]):
    discovered.append(node) # 탐색한 노드에 추가
    for x in graph[node]: # 해당 노드 하위의 모든 노드
        if x not in discovered: # 탐색한 적 없으면
            discovered = recursion_dfs(x, discovered) # 재귀 함수 실행
    return discovered #최종 탐색 결과

# Stack 이용한 DFS
# Input : 루트 노드 값
def stack_dfs(node):
    discovered = []
    stack = [node] #최초 루트 노드
    while stack: # 스택이 빌 때 까지
        v = stack.pop() # 스택에서 꺼내옴
        if v not in discovered: # 탐색한 적이 없으면
            discovered.append(v) # 탐색한 노드에 추가
            for w in graph[v]: # 해당 노드의 모든 하위 노드
                stack.append(w) # 스택에 추가
    return discovered #최종 탐색 결과

print("="*5,"Recursion","="*5)
print( recursion_dfs(1) )

print("="*5,"Stack","="*5)
print( stack_dfs(1) )


