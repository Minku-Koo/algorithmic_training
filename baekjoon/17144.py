"""
Date : 21.04.22
Problems : https://www.acmicpc.net/problem/17144
Title : 미세먼지 안녕! 0600
"""

class Dust:
    def __init__(self, r, c, t, room):
        self.r, self.c, self.t = r, c, t
        self.room = room
        self.cleaner = []

        # 공기청정기 위치 식별
        for y in range(self.r):
            for x in range(self.c):
                if self.room[y][x] == -1:
                    self.cleaner = [y, y+1]
                    break

    def expandDust(self):
        newMap = [ [0 if i!=-1 else -1 for i in x] for x in self.room]
        for y in range(self.r):
            for x in range(self.c):
                dust = self.room[y][x]
                if dust == -1: continue
                
                expandCount = [0, 0, 0, 0] # 상 우 하 좌
                # 확산될 수 있는 방향 계산
                if y>0 and self.room[y-1][x]!=-1: expandCount[0] +=1
                if y<self.r-1 and self.room[y+1][x]!=-1: expandCount[2] +=1
                if x>0 and self.room[y][x-1]!=-1: expandCount[3] +=1
                if x<self.c-1 and self.room[y][x+1]!=-1: expandCount[1] +=1

                exist, expandDust = self.calcDust(sum(expandCount), dust)

                if expandCount[0]: # 상
                    newMap[y-1][x] += expandDust
                if expandCount[1]: # 우
                    newMap[y][x+1] += expandDust
                if expandCount[2]: # 하
                    newMap[y+1][x] += expandDust
                if expandCount[3]: # 좌
                    newMap[y][x-1] += expandDust

                if sum(expandCount) > 0:
                    newMap[y][x] += exist
        self.room = [ x[:] for x in newMap]
        
        return self.room


    # 미세먼지 확산되는 양과 잔여량 계산
    def calcDust(self, n, mount):
        expand = mount // 5
        exist = mount - expand * n
        return exist, expand

    # 공기청정기 작동
    def removeDust(self, p):
        loc = self.cleaner[0] if p==1 else self.cleaner[1]
        loc -= 1
        
        if p==1:
            for y in range(loc-2, -1, -1):
                self.room[y+1][0] = self.room[y][0]
            for x in range(self.c-1): #위
                self.room[0][x] = self.room[0][x+1]
            for y in range(loc):
                self.room[y][-1] = self.room[y+1][-1]
            for x in range(self.c-1, 0, -1):
                self.room[loc][x] = self.room[loc][x-1]
                if self.room[loc][x] == -1: self.room[loc][x] = 0


        else:
            for y in range( loc+1, self.r-1):
                self.room[y][0] = self.room[y+1][0]
            for x in range(self.c-1): #위
                self.room[self.r-1][x] = self.room[self.r-1][x+1]
            for y in range( self.r-1, loc, -1):
                self.room[y][-1] = self.room[y-1][-1]
            for x in range(self.c-1, 0, -1):
                self.room[loc][x] = self.room[loc][x-1]
                if self.room[loc][x] == -1: self.room[loc][x] = 0
        
        
        return


if __name__ == "__main__":
    r, c, t = list(map(int, input().split()))
    room = []
    for _ in range(r): room.append(list(map(int, input().split())))

    dust = Dust(r, c, t, room)
    for _ in range(t):
        dust.expandDust()
        dust.removeDust(1)
        dust.removeDust(0)

    result = 0
    for j in dust.room: result += sum(j)
    print(result + 2)
