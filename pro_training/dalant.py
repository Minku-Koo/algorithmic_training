#

def list_gop(arr):
    n = 1
    for i in arr: n *= i
    return n

def solution(dalant, case):
    maxval = [0]
    
    def dfs(k, stack = []):
        sm_stack = sum(stack)
        if k*(case-len(stack)) + sm_stack > dalant: return
        
        if len(stack)+1 == case:
            stack.append( dalant - sm_stack )
            # dfs(k, stack)
            calc = list_gop(stack)
            if maxval[0] < calc: maxval[0] = calc
            stack.pop()
        else:
            for j in range(k, min(k+2, dalant-case*(k-1))): #dalant - case*(k-1)):
                stack.append(j)
                dfs(k, stack)
                stack.pop()
                
        return 
    
    
    # for k in range(dalant//case, dalant//case+1):
        # dfs(k, [k])
    k =  dalant//case
    klist = [k for _ in range( (case - (dalant%case)-1 ))]
    klist += [k+1 for _ in range( (dalant%case)-1 )]
    # print(klist)
    # dfs(k, [k])
    dfs(k, klist)
    return maxval[0]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dalant, case = list(map( int, input().split() ))
    print(f"#{test_case} {solution(dalant, case )}")



#1 36
#2 1024
#3 46656
#4 1679616
#5 26214400
#6 2448880128
#7 125524238436
#8 2821109907456
#9 162679413013056
#10 5856458868470016


