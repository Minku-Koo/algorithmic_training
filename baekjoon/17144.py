"""
Date : 21.04.22
Problems : https://www.acmicpc.net/problem/17144
Title : 미세먼지 안녕!
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
    
    # 미세먼지 확산
    def expandDust(self):
        # 기존 미세먼지 위치 정보 복사
        newRoom = [ [0 if i!=-1 else -1 for i in x] for x in self.room]
        for y in range(self.r):
            for x in range(self.c):
                dust = self.room[y][x]
                if dust == -1: continue # 공기 청정기일 경우 제외
                if dust == 0: continue # 미세먼지 없는 경우 제외
                
                expand_way = [0, 0, 0, 0] # 상 우 하 좌
                # 확산될 수 있는 방향 계산
                # 공기청정기 있거나, 벽이면 제외
                if y>0 and self.room[y-1][x]!=-1: expand_way[0] +=1
                if y<self.r-1 and self.room[y+1][x]!=-1: expand_way[2] +=1
                if x>0 and self.room[y][x-1]!=-1: expand_way[3] +=1
                if x<self.c-1 and self.room[y][x+1]!=-1: expand_way[1] +=1

                # 미세먼지 잔여량과 확산량 계산
                exist, expand_dust = self.calcDust(sum(expand_way), dust)

                if expand_way[0]: # 상
                    newRoom[y-1][x] += expand_dust
                if expand_way[1]: # 우
                    newRoom[y][x+1] += expand_dust
                if expand_way[2]: # 하
                    newRoom[y+1][x] += expand_dust
                if expand_way[3]: # 좌
                    newRoom[y][x-1] += expand_dust

                if sum(expand_way) > 0: # 확산되었다면
                    newRoom[y][x] += exist
        
        # 확산된 미세먼지 정보 입력
        self.room = [ x[:] for x in newRoom]
        
        return self.room


    # 미세먼지 확산되는 양과 잔여량 계산
    def calcDust(self, n, mount):
        expand = mount // 5 # 5로 나누고, 나머지 버림
        exist = mount - expand * n
        return exist, expand

    # 공기청정기 작동
    def removeDust(self, p):
        # 공기청정기 위치 파악 (위쪽: p=1, 아래쪽: p=0)
        loc = self.cleaner[0] if p==1 else self.cleaner[1]
        loc -= 1
        
        if p==1: # 위쪽 공기청정기 회전
            for y in range(loc-2, -1, -1): # 왼쪽
                self.room[y+1][0] = self.room[y][0]
            for x in range(self.c-1): # 위쪽
                self.room[0][x] = self.room[0][x+1]
            for y in range(loc): # 오른쪽
                self.room[y][-1] = self.room[y+1][-1]
            for x in range(self.c-1, 0, -1): # 아래쪽
                self.room[loc][x] = self.room[loc][x-1]
                if self.room[loc][x] == -1: self.room[loc][x] = 0


        else: # 아래쪽 공기청정기 회전
            for y in range( loc+1, self.r-1):
                self.room[y][0] = self.room[y+1][0]
            for x in range(self.c-1): 
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
        dust.expandDust() # 미세먼지 확산
        dust.removeDust(1) # 위쪽 공기청정기 회전 
        dust.removeDust(0) # 아래쪽 공기청정기 회전

    result = 0 # 총 합 계산
    for j in dust.room: result += sum(j)
    print(result + 2)
