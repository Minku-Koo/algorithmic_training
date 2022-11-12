'''
Two Pointer
'''

def solution(gems):
    answer = [0, 0]
    kindLen = len(set(gems))    # 보석 종류
    gemLen = len(gems)          # 전체 길이
    kindDict = {gems[0]:1}      # 현재 범위에서 보석 종류 갯수
    start, end = 0, 0           # start point, end point
    minLen = 100000             # min값 초기화

    while end < gemLen:
        if len(kindDict.keys()) != kindLen: # 모든 보석 다 없다면
            end += 1
            if end == gemLen:   # 범위 벗어나면 종료
                break
            kindDict[gems[end]] = kindDict.get(gems[end], 0) + 1
        else:   # 모든 보석 다 있다면
            if end - start < minLen:    # 최솟값이면
                minLen = end - start
                answer = [start + 1, end + 1]
            # 범위 내 보석 종류 갱신
            if kindDict[gems[start]] > 1:
                kindDict[gems[start]] -= 1
            else:
                del kindDict[gems[start]]
            
            if start < end:
                start += 1
            
    return answer