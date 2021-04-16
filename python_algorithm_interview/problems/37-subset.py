# 21.04.17
# p.355
# Problem Title : 부분 집합

def solution(nums):
    max = len(nums) # 부분 집합 최대값
    result = []
    subset = []
    
    def dfs(nums, depth = 0): # DFS 이용하여 계산
        # nums : 다음에 올 수 있는 숫자 집합
        # depth : 부분 집합 크기

        #최대 부분 집합 크기보다 클 경우
        if depth > max:  return 

        if depth == len(subset): # 부분 집합 크기와 같을 경우
            result.append(subset[:]) # 결과에 추가
            
        for w in nums: # 다음에 올 숫자 반복
            subset.append(w) # 해당 숫자 추가
            index = nums.index(w) # 해당 숫자 인덱스
            nextLine = nums[index+1:] # 해당 숫자 이후 숫자 집합 전달
            dfs(nextLine, depth + 1) #재귀 함수
            subset.pop() # 마지막 숫자 제거

        return

    dfs(nums)

    return result


if __name__ == "__main__":
    nums = [1,2,3,4]
    result = solution(nums)
    print("result:", result)
