# 31.04.16
# p.341
# Problem Title : 순열

def solution(number):
    result = []
    permute=[]
    def dfs(numbers): # DFS를 이용, 모든 순열 계산
        if len(permute) == len(number): # 숫자가 다 채워지면
            result.append(permute[:]) # 결과에 추가
            
        for num in numbers: # 다음 올 수 있는 숫자 반복
            permute.append(num) # 순열에 숫자 추가
            new_number = numbers[:]
            # 다음에 올 수 있는 숫자에서, 현재 숫자 제거 
            new_number.remove(num) 
            dfs(new_number) # DFS 재귀
            permute.pop() # 현재 숫자 제거
            
        return 

    dfs(number)
    
    return result

if __name__ == "__main__":
    number = [3,5,2,8]
    result = solution(number)
    print("Count Permutation:", len(result))
    print("Permutation:", result)
    
