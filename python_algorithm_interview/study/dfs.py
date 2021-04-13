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
def recursion_dfs(node, discovered=[]):
    discovered.append(node)
    for x in graph[node]:
        if x not in discovered:
            discovered = recursion_dfs(x, discovered)
    return discovered

# Stack 이용한 DFS
def stack_dfs(node):
    discovered = []
    stack = [node]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

print("="*5,"Recursion","="*5)
print( recursion_dfs(1) )

print("="*5,"Stack","="*5)
print( stack_dfs(1) )


