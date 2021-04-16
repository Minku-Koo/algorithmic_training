# 21.04.16
# p.351
# Problem Title : 조합의 합 (원소 중복 허용)

def solution(candidates, target):
    result = []
    
    def dfs(element): # DFS를 이용하여 계산
        if sum(combines) == target: # 조합 합이 target과 같으면
            result.append(combines[:]) # 결과에 추가

        index = candidates.index(element) # 해당 숫자 인덱스
        for num in candidates[index:]: # 인덱스 뒷 숫자 iteration
            combines.append(num) # 조합에 추가
            if sum(combines) <= target: # target보다 같거나 작으면
                dfs(num) # 재귀 함수
                combines.pop() # 마지막 원소 제거
            else:
                combines.pop() # 마지막 원소 제거

        return

    for num in candidates: # 해당 원소를 루트 노드로 설정
        combines = [num] # 조합에 루트 노드 추가
        dfs(num) # DFS 함수 시작

    return result

if __name__ == "__main__":
    candidates = [2,3,4,7]
    target = 12
    result = solution(candidates, target)
    print("result:", result)