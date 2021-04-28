"""
Date : 21.04.19
Problems : https://www.acmicpc.net/problem/16234
Title : 인구 이동
"""

class Move:
    def __init__(self, N, L, R, people):
        self.N = N
        self.L = L
        self.R = R
        self.people = people
        self.unions  = []

    def openBorder(self): # 국경 열어주는 함수
        result = []
        L, R = self.L, self.R
        
        def dfs(y, x, check = []): #DFS 이용하여 계산
            nowNation = self.people[y][x] # 현재 국가
            check.append( (y, x) ) # 현재 국가 좌표 추가
            # 결과에 추가할지 여부, 연합할 국가가 있다면, 바로 추가하지 않음
            plus = True 
            
            # 방문하지 않았고, 이전 국가가 있는 경우
            if (y-1, x) not in check and y>0 : 
                # 이전 국가와 같이 않으면 (시간 단축 위한 조건)
                if self.people[y-1][x] != nowNation: 
                    # 범위 내의 인구 수 차이면
                    if  ( L <= abs(self.people[y-1][x] - nowNation) <= R):
                        dfs(y-1, x, check) # DFS 재귀 함수
                        plus = False # 추가하지 않음

            
            if (y+1, x) not in check and y<self.N-1 :
                if self.people[y+1][x] != nowNation:
                    if ( L <= abs(self.people[y+1][x] - nowNation) <= R):
                        dfs(y+1, x, check)
                        plus = False

            
            if (y, x-1) not in check and x>0 :
                if self.people[y][x-1] != nowNation:
                    if  ( L <= abs(self.people[y][x-1] - nowNation) <= R):
                        dfs(y, x-1, check)
                        plus = False
                    
            
            if (y, x+1) not in check and x<self.N-1 :
                if self.people[y][x+1] != nowNation:
                    if ( L <= abs(self.people[y][x+1] - nowNation) <= R):
                        dfs(y, x+1, check)
                        plus = False

            # 추가할 수 있고, 2개 이상 국가의 연합인 경우
            if plus and len(check) > 1: temp.extend(check[:])

            return

        visited = [] # 방문한 국가
        for y in range(self.N):
            for x in range(self.N):
                if (y, x) not in visited: #방문하지 않았다면
                    temp = [] # 초기화
                    dfs(y, x, []) # 연합 국가 계산
                    union = list(set(temp)) # 연합 국가 집합 리스트
                    # 2개 이상의 연합, 결과에 없으면
                    if len(union) >1 and union not in result : 
                        result.append( union ) # 결과 추가
                        visited.extend( union ) # 방문한 국가 추가
        
        self.unions = result
        
        if len(result) > 0: return True # 결과가 있으면
        else: return False # 결과가 없으면 -> 프로그램 종료

    def movePeople(self): # 인구 이동 함수
        for union in self.unions: # 연합된 국가 리스트
            # 이동된 인구 계산
            divPeople = sum([ self.people[y][x] for y, x in union]) // len(union)
            # 연합 국가에 인구 입력
            for y, x in union: self.people[y][x] = divPeople
        return

if __name__ == "__main__":
    N, L, R = map(int, input().split())
    people = []
    for _ in range(N): people.append( [ int(x) for x in input().split() ]  )
    
    count = 0 # 전체 이동 횟수
    move_people = Move(N, L, R, people) # 클래스 선언
    while move_people.openBorder(): # 만약 연합 국가가 있다면
        move_people.movePeople() # 인구 이동
        count += 1 # 횟수 추가
        
    print( count)

