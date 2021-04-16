# 21.04.16
# p.346
# Problem Title : 조합

def solution(n, k):
    result = []
    combine = []
    #최초 1~n 숫자 정렬
    numRange = [ x for x in range(1, n+1) ]

    def dfs(numbers): # DFS를 이용한 조합 계산
        if len(combine) == k: #숫자가 k개 생성되면
            result.append(combine[:]) # 결과에 추가
            
        for num in numbers: # 다음에 위치할 숫자 리스트
            combine.append(num) # 조합에 추가
            # 현재 숫자 제외, 다음에 올 수 있는 숫자 리스트 생성
            new_numbers = numRange[num:] 
            dfs(new_numbers) #재귀함수
            combine.pop() # 마지막 숫자 제거하고 다시 반복
            
        return

    dfs( numRange )
    
    return result

if __name__ == "__main__":
    n = 7
    k = 3
    result = solution(n, k)
    print("Count Combine:", len(result))
    print("Combine:", result)
    
