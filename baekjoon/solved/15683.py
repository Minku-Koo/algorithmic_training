"""
Date : 21.04.22
Problems : https://www.acmicpc.net/problem/15683
Title : 감시
"""

class Cctv:
    def __init__(self, n, m, room):
        self.n = n
        self.m = m
        self.room = room
        self.cctv,  self.wall = self.getCctv()
    
    # cctv 위치 파악
    def getCctv(self):
        cctv, wall = [], [] # cctv와 벽 위치
        for y in range(self.n):
            for x in range(self.m):
                cell = self.room[y][x]
                # cctv
                if 1<= cell <= 5: cctv.append((y,x))
                # 벽
                if cell == 6: wall.append((y,x))
        return cctv, wall

    # 감시 범위에 따라 감시 가능한 위치 확인
    def checkCctv(self, y, x, see = [0, 0, 0, 0]):
        check = [] # cctv가 볼 수 있는 위치
        if see[0] == 1: # 상
            # cctv 위치에서 방 끝까지
            for y_ in range(y, -1, -1):
                # 벽에 막힐 경우 > 종료
                if self.room[y_][x] == 6: 
                    break
                else:
                    check.append((y_, x))
        if see[1] == 1: # 우
            for x_ in range(x, self.m):
                if self.room[y][x_] == 6:
                    break
                else:
                    check.append((y, x_))
        if see[2] == 1: # 하
            for y_ in range(y, self.n):
                if self.room[y_][x] == 6:
                    break
                else:
                    check.append((y_, x))
        if see[3] == 1: # 좌
            for x_ in range(x, -1, -1):
                if self.room[y][x_] == 6:
                    break
                else:
                    check.append((y, x_))

        return check

    # cctv 종류에 따른 방향 설정
    def kindWay(self, num):
        way = [] # 방향
        
        if num == 1: # 1번 cctv
            for i in range(4):
                temp = [0,0,0,0]
                temp[i] = 1
                way.append( temp )

        elif num==2:
            way.append([1, 0, 1, 0])
            way.append([0, 1, 0, 1])

        elif num==3:
            way.append([1, 1, 0, 0])
            way.append([0, 1, 1, 0])
            way.append([0, 0, 1, 1])
            way.append([1, 0, 0, 1])
                
        elif num==4:
            for i in range(4):
                temp = [1,1,1,1]
                temp[i] = 0
                way.append( temp )
        else: # 5
            way.append( [ 1,1,1,1 ] )
        
        return way
    
    # 결과 확인
    def getMin(self):
        result = [] # 감시할 수 있는 좌표 리스트
        check_cctv = [] # 검사한 cctv
        see_in_room = [] # 감시할 수 있는 좌표

        def dfs(num = 0): # DFS를 이용하여 계산, index 0부터 시작
            if len(check_cctv) == len(self.cctv): # 모든 cctv 다 검사
                result.append( see_in_room[:] )
                return

            y, x = self.cctv[num] # cctv 위치 받아옴
            
            # cctv 위치에서 확인 가능한 경우의 수
            for way in self.kindWay(self.room[y][x]): 
                check_cctv.append( (y, x) ) # cctv 위치 추가
                # 현재 cctv에서 확인 가능한 좌표 추가
                see_in_room.append( self.checkCctv(y, x, see = way) )
                
                dfs(num+1) # 다음 index 확인
                see_in_room.pop() # 현재 cctv 확인 경로 제거
                check_cctv.pop()
            
            return
        
        dfs()

        maxVal =0 # 최대 확인 가능한 위치

        for case in result: # 확인 가능한 경우의 수
            temp = []
            for c in case: temp.extend(c)
            # 확인 가능한 경우의 수 > 중복 제거
            case_result = list(set(temp))
            if maxVal < len(case_result): # 기존 최대값보다 크면
                maxVal = len(case_result)
                
        return  maxVal


if __name__ == "__main__":
    n, m = map(int, input().split())
    room = []
    for _ in range(n): room.append( list(map(int, input().split())) )

    cctv = Cctv(n, m, room)
    max_val = cctv.getMin()
    # 방 전체에서 확인 가능한 공간 제거 = 사각지대
    result = n * m - ( max_val + len(cctv.wall) ) 
    print(result)

