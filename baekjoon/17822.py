"""
Date : 21.04.21
Problems : https://www.acmicpc.net/problem/17822
Title : 원판 돌리기
"""

class Circle:
    def __init__(self, N, M, T, maps, orders ):
        self.N, self.M, self.T = N, M, T
        self.map = maps
        self.order = orders

    # x번째 판 회전해주는 함수
    def moving(self, x, d, k):
        new_map = self.map[:][x-1] #해당 원 가지고오기
        if d == 0: #시계방향
            for _ in range(k): # x 배수, k 번 회전
                temp = new_map.pop() # 제일 마지막 원소
                new_map.insert(0, temp) # 제일 앞으로
        else: #반시계 방향
            for _ in range(k):
                temp = new_map.pop(0) # 제일 앞 원소
                new_map.append(temp) # 제일 마지막으로
        self.map[x-1] = new_map # 원판에 입력
        return

    # 인접 숫자 지우기
    def eraseNum(self):
        
        def sameNum(): # 인접한 숫자 찾는 함수
            sameNumbers = [] # 인접한 숫자 위치 리스트
            for y in range(len(self.map)):
                for x in range(len(self.map[0])):
                    number = self.map[y][x]
                    if number == 0: continue # 0이면 제외
                    
                    if  y<self.N -1 :
                        if self.map[y+1][x] == number: # 상
                            sameNumbers.append( (y+1, x) )
                    if  y>0 :
                        if self.map[y-1][x] == number: # 하
                            sameNumbers.append( (y-1, x) )

                    if  x>0 :
                        if self.map[y][x-1] == number: # 좌
                            sameNumbers.append( (y, x-1) )

                        if x==self.M-1:
                            if self.map[y][0] == number: # 우
                                sameNumbers.append( (y, 0) )

                    if  x<self.M-1 :
                        if self.map[y][x+1] == number: # 양 옆 
                            sameNumbers.append( (y, x+1) )

                        if x==0:
                            if self.map[y][self.M-1] == number: # 양 옆
                                sameNumbers.append( (y, self.M-1) )

            return list(set(sameNumbers)) # 중복 제거 후 반환
                    
        same = sameNum() # 인접한 숫자 위치 받아옴
        
        if  len(same)>1: # 인접한 숫자가 있다면
            for i, j in same: 
                # 0으로 바꾸어줌
                self.map[i][j] = 0
        
        else: # 인접한 숫자가 없다면
            sumMap, count = 0, 0
            for line in self.map: 
                # 0 개수 제외하고 카운트
                count += self.M - line.count(0)
                # 총 합 계산
                sumMap += sum(line)
            
            # 총 합이 0이라면
            if sumMap ==0: average = 0 # 평균 0
            else: average = sumMap / count # 평균 계산

            for y in range(self.N):
                for x in range(self.M):
                    number = self.map[y][x]
                    if number == 0: continue # 0 제외
                    if number < average: # 평균보다 작으면
                        self.map[y][x] += 1 # +1
                    elif number > average: # 평균보다 크면
                        self.map[y][x] -= 1 # -1
                        
        return 


if __name__ == "__main__":
    N, M, T = list(map(int, input().split()))
    maps = []
    for _ in range(N): maps.append(list(map(int, input().split())))
    orders = []
    for _ in range(T): orders.append(list(map(int, input().split())))

    circle = Circle(N, M, T, maps, orders) # 클래스 선언
    
    for x, d, k in orders: # 명령 전달
        max_ = N // x # 실행 횟수
        for m in range(1, max_+1): 
            circle.moving(x*m, d, k) # 원판 움직임
        circle.eraseNum() # 인접 숫자 지우기
        
    result = 0
    # 총 합 계산
    for j in circle.map: result += sum(j)  
    print(result)
    
    