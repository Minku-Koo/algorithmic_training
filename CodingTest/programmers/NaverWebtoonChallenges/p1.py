
'''
# date : 21.07.04
'''


def solution(S, pattern):
    answer = 0

    length = len(pattern) #패턴길이
    strings, permute = [], []
    def dfs(pt): # DFS를 이용, 모든 순열 계산
        if len(permute) == length: # 문자가 다 채워지면
            strings.append( "".join(permute) ) # 결과에 추가
            
        for num in pt: # 다음 올 수 있는 문자 반복
            permute.append(num) # 순열에 문자 추가
            new_number = [x for x in pt]
            # 다음에 올 수 있는 문자에서, 현재 문자 제거
            new_number.remove(num) 
            dfs(new_number) # DFS 재귀
            permute.pop() # 현재 문자 제거
            
        return 

    dfs(pattern) # 문자열 순열 계산

    def checkInner(string, s): # 해당 패턴이 문자열에 포함되는 개수
        l = len(string) # 최소 길이
        count = 0 
        for index, chr in enumerate(s):
            if index+l >len(s): # 끝까지 반복
                break
            stemp = s[index: index+l ] # 문자열 추출

            if stemp == string: # 추출된 문자열과 패턴이 같다면
                count += 1

        return count


    chechedString = []
    for string in strings:
        if string in chechedString:  # 이미 검사한 패턴일 경우
            continue
        # if string in S:
        checked = checkInner(string, S)
        if checked>0: # 하나라도 포함된 경우
            answer += checked
            chechedString.append(string)


    return answer

s = "wreawerewa"
pat = "ware"

rr = solution(s, pat)
print(rr)




