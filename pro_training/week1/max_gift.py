import itertools
def solution( number, count ):
    result = 0
    LENGTH = len(number)
    check_dict = {
        # "123456": [2, 3]
    }
    def getBranch(num):
        # 숫자에 맞는 모든 경우의수 반환
        return list(itertools.combinations(range(num), 2))
    
    queue = [(number, 0)]
    while queue:
    
        node, change = queue.pop(0) # 바꿀 두 위치, 바꾼 횟수
        
        if change==count: 
            if int(node) > result:  result = int(node)
            continue
            
        for y, x  in getBranch(LENGTH):
            node_ = [g for g in node]
            node_[y], node_[x] = node[x], node[y]
            input_node = ''.join(node_) 
            if int(input_node)<=result: continue
            
            if not check_dict.get(input_node)  :
                queue.append(( input_node , change+1))
                check_dict[input_node] = [change+1]
            elif change+1 not in check_dict.get(input_node): 
                queue.append(( input_node , change+1))
                check_dict[input_node].append(change+1)
            else: continue
            
            pass
        
    return result

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    number, count = list(input().split())
    print("#"+str(test_case) , end=" ")
    print( solution( number, int(count) ) )
    
    