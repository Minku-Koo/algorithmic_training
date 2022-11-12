'''
Sorting and Greedy
'''
def solution(routes):
    answer = 0
    camera = -300000
    
    routes = sorted(routes, key=lambda x:x[1])  # end 기준으로 정렬
    for log in routes:
        if camera < log[0]: # 기존 카메라와 겹치지 않을 경우
            answer += 1
            camera = log[1]

    return answer

