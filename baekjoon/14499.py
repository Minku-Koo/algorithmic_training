"""
Date : 21.04.18
Problems : https://www.acmicpc.net/problem/14499
Title : 주사위 굴리기
"""

class Dice:
    def __init__(self, N, M, x, y, k, maps):
        self.N = N
        self.M = M
        self.x = x
        self.y = y
        self.k = k
        self.map = maps # 지도
        self.bottom = 6 # 바닥
        self.front = 5 # 앞
        self.west = 4 # 서쪽
        self.dice = { # 주사위
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        }
        

    # 방향 입력
    # 주사위 모양 변경
    def changeDice(self, moving):
        # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
        # 바깥으로 벗어나려 하면, 명령 무시
        if (self.y == 0 and moving == 3) or \
        (self.y == self.N-1 and moving == 4) or \
        (self.x == 0 and moving == 2) or \
        (self.x == self.M-1 and moving == 1) :
            return False
        
        if moving == 1: # 동쪽
            temp = self.bottom
            self.bottom = 7 - self.west
            self.west = temp
            self.x += 1
        elif moving == 2: # 서쪽
            temp = self.bottom
            self.bottom = self.west
            self.west = 7 - temp
            self.x -= 1
        elif moving == 3: # 북쪽
            temp = self.front
            self.front = 7 - self.bottom
            self.bottom = temp
            self.y -= 1
        elif moving == 4: # 남쪽
            temp = self.front
            self.front = self.bottom
            self.bottom = 7 - temp
            self.y += 1

        return True
    
    # 지도와 주사위 숫자 변경
    def changeMapDiceNumber(self):
        if self.map[self.y][self.x] == 0:
            self.map[self.y][self.x] = self.dice[self.bottom]
        else:
            self.dice[self.bottom] = self.map[self.y][self.x]
            self.map[self.y][self.x] = 0
        return



if __name__ == "__main__":
    
    N, M, y, x, k = [ int(x) for x in input().split() ]
    maps = []
    for _ in range(N):
        maps.append( [ int(x) for x in input().split()] )

    moving = [ int(x) for x in input().split()]
    

    d = Dice(N, M, x, y, k, maps) #클래스 선언
    for m in moving: # 명령 하나씩
        if d.changeDice(m): # 만약 바깥으로 벗어나지 않으면
            d.changeMapDiceNumber() # 지도와 주사위 숫자 변경
            print( d.dice[7 - d.bottom] ) # 주사위 위쪽 출력
    


