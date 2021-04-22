"""
Date : 21.04.22
Problems : https://www.acmicpc.net/problem/19237
Title : 어른 상어
"""

class AdultShark:
    def __init__(self, n, m, k, map, shark_dir, shark_move_first):
        self.n, self.m, self.k = n, m, k
        self.map = map
        self.shark = {}
        # 최초 상어 위치
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] != 0: self.shark[ self.map[y][x] ] = (y, x)
        
        self.shark_dir = shark_dir
        self.shark_move_first = {}
        # key: 상어 번호 / value: 상어별 우선순위
        for index in range(0, len(shark_move_first), 4):
            if index % 4 == 0:
                num = index // 4
                self.shark_move_first[num+1] = shark_move_first[index:index+4]
        # 냄새 지도 초기화 
        self.smellMap = [ [ (0, 0) for i in x] for x in map]
        # 최초 상어 존재 위치에 냄새 남기기
        for key in self.shark:
            y, x = self.shark[key]
            self.smellMap[y][x] = (key , self.k)

    # 상어 우선순위 계산 
    def checkSharkMoveFisrt(self, sharkNum):
        # 현재 상어 방향
        now_dir = self.shark_dir[sharkNum-1]
        # 현재 방향을 고려한 우선순위
        dir_first = self.shark_move_first[sharkNum][now_dir - 1]
        return dir_first

    # 현재 위치, 이동 방향을 통해 새로운 좌표 설정
    def getNewLoc(self, y, x, dir):
        if dir == 1: return y-1, x
        elif dir == 2: return y+1, x
        elif dir == 3: return y, x-1
        else: return y, x+1

    
    # 상어 이동
    def moveShark(self):
        for shark_num in self.shark :
            dir = self.shark_dir[shark_num-1] # 현재 상어 방향
            y, x = self.shark[shark_num] # 현재 상어 위치

            # 1 위 2 아래 3 좌 4 우
            goal_none = [] # 아무 냄새 없는 리스트
            goal_mine = [] # 자기 냄새 리스트
            goal_other = [] # 다른 냄새 리스트
            
            # 방향 설정
            if y > 0:  # 위
                num = 1
                # 아무 냄새 없으면
                if self.smellMap[y-1][x][0] == 0 : goal_none.append(num)
                # 자기 냄새
                if self.smellMap[y-1][x][0] == shark_num: goal_mine.append(num)
                # 다른 냄새
                elif self.smellMap[y-1][x][0] > 0:  goal_other.append(num)
                

            if y < self.n -1: # 아래
                num = 2
                if self.smellMap[y+1][x][0] == 0 : goal_none.append(num)
                if self.smellMap[y+1][x][0] == shark_num: goal_mine.append(num)
                elif self.smellMap[y+1][x][0] > 0:  goal_other.append(num)
                

            if x > 0: # 좌
                num = 3
                if self.smellMap[y][x-1][0] == 0 : goal_none.append(num)
                if self.smellMap[y][x-1][0] == shark_num: goal_mine.append(num)
                elif self.smellMap[y][x-1][0] > 0:  goal_other.append(num)
                

            if x < self.n -1: # 우
                num = 4
                if self.smellMap[y][x+1][0] == 0 : goal_none.append(num)
                if self.smellMap[y][x+1][0] == shark_num: goal_mine.append(num)
                elif self.smellMap[y][x+1][0] > 0:  goal_other.append(num)


            goal = []
            if goal_none != []: # 아무 냄새 없는 곳 존재하면
                goal = goal_none[:]
            elif goal_mine != []: # 자기 냄새 있는 곳 존재하면
                goal = goal_mine[:]
            elif goal_other != []: # 그 외, 모든 곳에 다른 냄새 있으면
                goal = goal_other[:]


            # 우선 순위 판단
            newDir = 0 # 이동할 방향
            # 현재 방향 고려한 우선순위 리스트 반환
            dir_first = self.checkSharkMoveFisrt( shark_num)
            for d in dir_first:
                if d in goal: # 갈 수 있는 방향 중 우선순위 높은 곳
                    newDir = d
                    break

            # 상어 위치 재설정
            y, x = self.getNewLoc(y, x, newDir) # 나아갈 방향의 좌표 받아옴
            self.shark[shark_num] = (y, x)

            # 상어 방향 재설정
            self.shark_dir[shark_num-1] = newDir

        return

    # 냄새 재설정
    def setSmellMap(self):
        shark_loc = [ self.shark[x] for x in self.shark] # 상어 위치 리스트
        for y in range(len(self.smellMap)):
            for x in range(len(self.smellMap[0])):
                
                if (y, x) in shark_loc: # 상어가 있으면
                    for s in self.shark: 
                        if (y, x) == self.shark[s]: # 상어 번호 확인
                            self.smellMap[y][x] = (s , self.k) 
                elif self.smellMap[y][x][0] == 0: # 냄새가 없으면
                    continue
                
                else: # 냄새가 있고 상어가 없으면
                    shark, smell = self.smellMap[y][x]
                    # 냄새가 사라진 경우
                    if smell == 1: self.smellMap[y][x] = (0, 0)
                    # 1 차감하여 재입력
                    else : self.smellMap[y][x] = (shark, smell - 1)

        return

    # 중복 상어 제거
    def delShark(self):
        same_shark, key_list = [], [] 
        copy_shark = {} # 상어 위치 복사
        for key in self.shark:
            copy_shark[key] =  self.shark[key]
            key_list.append(key) # 존재하는 상어 번호들

        # 오름차순 정렬 (중복 상어중 숫자 큰 상어 제거)
        for sharkNum in sorted(key_list): 
            if self.shark[sharkNum] in same_shark: # 중복이면
                self.shark.pop(sharkNum) # 숫자 큰 상어 제거
            else: # 중복 아니면
                same_shark.append(self.shark[sharkNum])
        return





if __name__ == "__main__":
    n, m, k = list(map(int, input().split()))
    maps = []
    for _ in range(n): maps.append( list( map(int, input().split()) ) )

    #상어 방향 입력
    shark_dir = list(map(int, input().split()))

    #상어 우선순위 입력
    shark_move_first = []
    for _ in range(m*4): shark_move_first.append(list( map(int, input().split()) ) )


    sharks = AdultShark(n, m, k, maps, shark_dir, shark_move_first)
    
    count = 0
    while True: # 1번 상어만 남을 때까지 반복
        sharks.moveShark() # 상어 이동
        sharks.delShark() # 중복 상어 제거
        sharks.setSmellMap() # 냄새 재설정
        
        count +=1
        if len(sharks.shark) == 1: # 1번 상어만 남으면
            break # 종료


        if count >= 1000:  # 1000회 이상 지속되면
            count = -1 # -1 출력
            break # 종료

    print(count)
