
def solution(letters, k):
    answer = ''
    abc = "abcdefghijklmnopqrstuvwxyz" # 알파벳 리스트

    result, combine = [], []
    last_letter = [0] #가장 나중 문자 인덱스

    def dfs(letters): # DFS를 이용한 조합 계산
        if len(combine) == k: #숫자가 k개 생성되면
            result.append( "".join(combine[:]) ) # 결과에 추가
            last_letter[0] = abc.index(combine[0]) #나중 단어 초기화
            return
            
        for i, s in enumerate(letters): # 다음에 위치할 숫자 리스트
            # 나중 단어보다 앞 순서인 단어일 경우
            if len(combine)==1 and abc.index(combine[0]) < last_letter[0]: continue
            combine.append(s) # 조합에 추가
            # 현재 숫자 제외, 다음에 올 수 있는 숫자 리스트 생성
            
            new_letters = letters[i+1:] 
            dfs(new_letters) #재귀함수
            combine.pop() # 마지막 숫자 제거하고 다시 반복
            
        return

    dfs( letters )
    
    sorted_result = sorted( result, reverse=True) # 알파벳순서 정렬
    
    return sorted_result[0]

letters = "zbgaj"
k = 3
rr = solution(letters, k)
print(rr)
