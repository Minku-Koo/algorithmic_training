"""
Date : 21.04.23
Problems : https://www.acmicpc.net/problem/14891
Title : 톱니바퀴
"""

class GearWheel:
    def __init__(self, wheel):
        self.wheel = wheel
        self.setRotation()

    # 톱니바퀴 하나 회전 함수
    def rotWheel(self, num, dir): 
        if dir == 1: # 시계 방향
            temp = self.wheel[num-1].pop()
            self.wheel[num-1].insert(0, temp)
        else: # 반시계 방향
            temp = self.wheel[num-1].pop(0)
            self.wheel[num-1].append(temp)
        return

    def setRotation(self): # 톱니바퀴 맞물리는 지점
        self.rotation = [ [self.wheel[0][2], self.wheel[1][6]],
                          [self.wheel[1][2], self.wheel[2][6]],
                          [self.wheel[2][2], self.wheel[3][6]],
                        ]
        return

    def change(self, num, dir): 
        # 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향
        self.rotWheel(num, dir) # 해당 톱니바퀴 돌리기
        dirs = [dir, dir] # 전후 방향 설정
        for i in range(num+1, 5): # 앞쪽 방향
            # 극이 다를 경우
            if self.rotation[i-2][0] != self.rotation[i-2][1]: 
                dirs[0] = dirs[0] * -1 # 방향 바꾸기
                self.rotWheel(i, dirs[0])
            # 극이 같을 경우
            else: break
                    

        for i in range(num-1, 0, -1):  # 뒤쪽 방향
            if i>0:
                if self.rotation[i-1][0] != self.rotation[i-1][1]:
                    dirs[1] = dirs[1] * -1
                    self.rotWheel(i, dirs[1])
                else: break
                
        return

if __name__ == "__main__":
    wheel = []
    for _ in range(4): wheel.append( [ int(x) for x in  input()] )

    k = int(input())
    order = []
    for _ in range(k): order.append( list(map(int, input().split())) )

    gear = GearWheel(wheel)
    for od in order:
        num, dir = od # 명령
        gear.change(num, dir) # 톱니바퀴 변경
        gear.setRotation() # 맞물리는 지점 재설정

    result, gop = 0, 1 # 결과, 곱셈
    for g in gear.wheel: # 톱니바퀴 12시 방향 확인
        result += g[0] * gop
        gop *= 2
    print(result)
