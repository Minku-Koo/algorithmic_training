
def solution(word):
    answer = 0
    words = "AEIOU"
    diction, permute = [], []
    def dfs(w): # DFS를 이용, 모든 순열 계산
        if permute != []: 
            diction.append( "".join(permute) )
        
        if len(permute) == 5: # 문자가 다 채워지면 종료
            return

        for num in w: # 다음 올 수 있는 문자 반복
            permute.append(num) # 순열에 문자 추가
            dfs(w) # DFS 재귀
            permute.pop() # 현재 문자 제거
            
        return 
    
    dfs(words)
    
    return diction.index(word) +1 


word = "AAAAE"
rr = solution(word)
print(rr)

word = "EIO"
rr = solution(word)
print(rr)
