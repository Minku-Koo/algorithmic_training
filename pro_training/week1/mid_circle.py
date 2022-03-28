
# 중위순회
class Node: # 바이너리 트리를 구성 할 노드 클래스 생성
    def __init__(self, data):
        self.data = data;
        self.left = None;
        self.right = None;
        
def cr_graph(t):
    g = {}
    
    return 

def solution(node, tree):
    alpha = {}
    for j in range(node):
        root, chr = tree[j][:2]
        if len( tree[j] )==3:
            ln = tree[j][2]
        elif len( tree[j] )==4:
            ln, rn = tree[j][2:]
    
    return 



T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    node = int(input())
    tree = []
    for _ in range(node):
        inpt = list(map(int, input().split()))
        [ for x in range(4) ]
        tree.append(  list(map(int, input().split())) )
    print(f"#{test_case} {solution( node, tree ) }")

