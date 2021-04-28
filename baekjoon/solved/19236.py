"""
Date : 21.04.24
Problems : https://www.acmicpc.net/problem/19236
Title : 청소년 상어
"""

class KidultShark:
    def __init__(self, shark):
        self.shark = shark


    # 물고기 이동
    # 물고기 하나씩 이동시킴
    # 물고기 번호, 지도, 상어 위치
    def fishMove(self, fish_num, sharkMap, loc):
        isreturn = False # 해당 물고기 번호 없으면
        for i in range(4):
            for j in range(4):
                if sharkMap[i][j][0] == fish_num:
                    y, x= i, j
                    isreturn = True #  물고기 있으면 위치 설정
                    break
        if not isreturn: return sharkMap
        
        fish_dir = sharkMap[y][x][1] # 물고기 방향

        while True:
            if fish_dir == 1:
                y_, x_ = y-1, x
            elif fish_dir == 2:
                y_, x_ = y-1, x-1
            elif fish_dir == 3:
                y_, x_ = y, x-1
            elif fish_dir == 4:
                y_, x_ = y+1, x-1
            elif fish_dir == 5:
                y_, x_ = y+1, x
            elif fish_dir == 6:
                y_, x_ = y+1, x+1
            elif fish_dir == 7:
                y_, x_ = y, x+1
            else:
                y_, x_ = y-1, x+1
            
            # 범위 밖이거나, 상어랑 만나면
            if y_ < 0 or x_ < 0 or y_>3 or x_ >3 or loc == (y_, x_):
                fish_dir += 1 # 방향 재설정
                if fish_dir ==9: fish_dir = 1 # 8 넘어가면 다시 1
                 
            else: # 해당 물고기와 위치 교환
                temp = sharkMap[y_][x_]
                sharkMap[y_][x_] = (fish_num, fish_dir)
                sharkMap[y][x] = temp
                
                break

        return sharkMap

    # 더이상 먹을 상어 있니?
    def checkMove(self, y, x, dir, shark):
        
        result = False # 종료 여부
        fishes = [] # 물고기 위치

        while True:
            if dir == 1:
                y_, x_ = y - 1, x
            elif dir == 2:
                y_, x_ = y - 1, x - 1
            elif dir == 3:
                y_, x_ = y, x - 1
            elif dir == 4:
                y_, x_ = y + 1, x - 1
            elif dir == 5:
                y_, x_ = y + 1, x
            elif dir == 6:
                y_, x_ = y + 1, x + 1
            elif dir == 7:
                y_, x_ = y, x + 1
            else:
                y_, x_ = y - 1, x + 1
            # 범위 밖이면
            if y_ < 0 or x_ < 0 or y_ > 3 or x_ > 3:
                return result, fishes # 반환
            elif shark[y_][x_] != (0, 0):
                result = True
                fishes.append((y_, x_))

            y, x = y_, x_ # 위치 재설정
            
        return result, fishes


    # 상어 이동
    def sharkMove(self):
        result = [] # 경우의 수 
        check = [] # 해당 경우의 수 총 합
        
        def dfs(y, x, shark_copy):
            shark_dir = shark_copy[y][x][1] # 상어 방향
            shark_copy[y][x] = (0, 0) # 해당 공간 0으로 설정

            for d in range(1, 17): # 물고기 이동
                shark_copy = self.fishMove(d, shark_copy, (y, x))
            # 프로그램 종료 여부 및 먹을 수 있는 물고기 위치 반환
            keep, shark_root = self.checkMove(y, x, shark_dir, [a[:] for a in shark_copy[:]])
            
            if not keep:
                result.append(sum(check[:]))
                return

            for y, x in shark_root:
                loc = (y, x) # 이동할 상어 위치
                eat = shark_copy[y][x][0] # 먹을 물고기 숫자
                check.append(eat)
                # 재귀 함수
                dfs(y, x, [ a[:] for a in shark_copy[:]])
                check.pop()

            return

        dfs(0, 0, [ a[:] for a in self.shark[:]] )
        
        return max(result)


if __name__ == '__main__':
    maps = []
    for _ in range(4): maps.append( list(map(int, input().split())) )
    
    shark = []
    for loc in maps:
        line = []
        for i in range(0, 8, 2): # (숫자, 방향) 으로 설정
            line.append( (loc[i], loc[i+1]) )
        shark.append(line)

    first = shark[0][0][0] # 최초 먹은 물고기 숫자
    kshark = KidultShark(shark)
    result = kshark.sharkMove()
    print(result + first)
