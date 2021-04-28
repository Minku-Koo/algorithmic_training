"""
Date : 21.04.22
Problems : https://www.acmicpc.net/problem/14503
Title : 로봇 청소기
"""

class Robot:
    def __init__(self, n, m , r, c, d, room):
        self.n, self.m = n, m
        self.robot_cleaner = [r, c, d] # 청소기 위치 및 방향
        self.room = room # 방 정보
        self.clean_place = [] # 청소한 위치

    def solution(self): # 메인 함수
        while True: # 종료까지 반복
            # 청소기 현재 위치 청소한 위치에 추가
            self.clean_place.append( (self.robot_cleaner[0], self.robot_cleaner[1]) )
            left, dir, nowBack = self.checkSide() # 왼쪽, 뒤쪽, 방향 확인
            
            if self.checkAllSide() : # 모든 방향 청소되었거나 벽
                if  self.room[nowBack[0]][nowBack[1]] == 1: #뒤쪽 벽일 경우
                    # 중복 제거하고 청소한 위치 추가하고 종료
                    self.clean_place = list(set( self.clean_place))
                    break
                else: # 뒤쪽 갈 수 있으면
                    # 방향 유지, 뒤로 한칸 이동
                    self.robot_cleaner = [nowBack[0], nowBack[1], self.robot_cleaner[-1]]

            # 청소 되지 않은 공간이고, 벽이 아닐 경우
            elif self.room[left[0]][left[1]] != 1 and (left[0], left[1] ) not in self.clean_place: 
                # 회전하고 전진해서 청소
                self.robot_cleaner[-1] =  dir # 방향 재설정
                self.robot_cleaner[0] =  left[0] # 청소기 위치 재설정
                self.robot_cleaner[1] =  left[1]
                # 청소한 위치에 없으면 > 추가
                if left not in self.clean_place: self.clean_place.append( left )

            # 벽일 경우 or 청소된 구역일 경우
            elif self.room[left[0]][left[1]] == 1 or ( left[0], left[1] ) in self.clean_place:  
                # 회전하고 다시 검사
                self.robot_cleaner[-1] =  dir # 위치 재설정
            
        return

    def checkSide(self): # 현재 방향 기준 > 왼쪽, 뒤쪽 확인
        # 현재 위치
        y, x = self.robot_cleaner[0], self.robot_cleaner[1]
        # 현재 방향
        dir = self.robot_cleaner[-1]

        if dir == 0: # 상
            dir = 3
            left = (y, x-1)
            nowBack = (y+1, x)
        elif dir == 1:  # 우
            dir = 0
            left = (y-1, x)
            nowBack = (y, x-1)
        elif dir==2: # 하
            dir = 1
            left = (y, x+1)
            nowBack = (y-1, x)
        else: # 좌
            dir = 2
            left = (y+1, x)
            nowBack = (y, x+1)
        return left, dir, nowBack
    
    # 모든 방향 청소 or 벽인지 확인
    def checkAllSide(self):
        # 청소기 현재 위치
        y, x = self.robot_cleaner[0], self.robot_cleaner[1]
        condition = False

        for y_, x_ in [(1,0),(0,1),(-1,0),(0,-1) ]: # 상하좌우 확인
            if (y+y_, x+x_) in self.clean_place or self.room[y+y_][x+x_] ==1: pass
            else: # 청소되어있지 않으면 > False 반환
                return False
        
        return True # 모든 방향 청소 or 벽이면 True 반환


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    r, c, d = list(map(int, input().split()))
    room = []
    for _ in range(n): room.append(list(map(int, input().split())))

    robot = Robot(n, m , r, c, d, room)
    robot.solution()
    print( len(robot.clean_place) )

