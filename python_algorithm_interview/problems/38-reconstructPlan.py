# 21.04.17
# p.357
# Problem Title : 일정 재구성 (알파벳 순서 정렬)

def solution(plans):
    result = []
    root = []

    def dfs(start, plan): # DFS를 이용하여 계산
        if len(plans) == len(root): # 일정이 모두 채워지면
            result.append(root[:]) # 결과에 추가
            return

        for p in plan: # 여행지를 하나씩
            # 도착지와 출발지가 같으면
            if p[0] == start[1]:
                root.append(p)
                newPlan = plan[:]
                newPlan.remove(p) # 현재 경유지 제거
                dfs(p, newPlan) # 재귀 함수
                root.pop()
        
        return

    for point in plans: # 최초 출발지 지정
        if point[0] == "J": # J에서 출발하는 경우만
            root.append(point)
            newPlan = plans[:]
            newPlan.remove(point)
            dfs(point, newPlan) # DFS 시작
            root = []
    
    # 알파벳 순서 정렬
    print(result)
    result = sorted(result, key = lambda x : x[0])[0]
    print(result)
    sortedResult = [ result[0][0] ]
    
    # 경유지 하나씩 입력
    for r in result: sortedResult.append( r[1] ) 
        
    return sortedResult


if __name__ == "__main__":
    plans = [ ["J", "S"], ["J", "A"], ["S", "A"], ["A", "J"], ["A", "S"] ]
    result = solution(plans)
    print("result:", result)


