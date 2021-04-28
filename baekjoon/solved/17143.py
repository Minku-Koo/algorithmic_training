"""
Date : 21.04.20
Problems : https://www.acmicpc.net/problem/17143
Title : 낚시왕 
"""

class Fishing:
    def __init__(self, R, C, M, shark):
        self.W, self.H = C, R
        self.shark = shark
        self.man = 0 # 낚시왕 위치
        self.sharkSize = 0 # 잡은 상어 크기

    # 전체 상어 이동 함수
    def sharkChange(self):
        samePlace = {} # 상어 위치 중복되는지? key: 좌표 / value : 상어 인덱스
        # 상어 이동
        for index, shark in enumerate(self.shark[:]):
            # y, x, 속도, 방향, 크기
            newShark = self.sharkMove(shark) # 상어 이동
            self.shark[index] = newShark
            y, x = newShark[0], newShark[1] # 새로운 상어 좌표
            # 위치 중복 확인을 위해 딕셔너리 입력
            if (y, x) in samePlace.keys(): samePlace[ (y, x) ].append(index)
            else: samePlace[ (y, x) ]  = [index]

        # 중복 상어 제거
        removeShark = []
        for y, x in samePlace.keys(): # 현재 상어 위치
            if len(samePlace[(y, x)]) >1: # 좌표에 2개 이상 상어 있으면
                maxSize = -1 # 상어 크기
                maxIndex = -1 # 제일 큰 상어 인덱스
                for index in samePlace[(y, x)]:
                    size = self.shark[index][-1] # 상어 크기 확인
                    if size > maxSize:  # 기존 상어보다 크면
                        maxSize = size
                        maxIndex = index

                removeList = samePlace[(y, x)][:] # 제거할 상어 인덱스 복사
                removeList.remove(maxIndex) # 제거할 상어중 가장 큰 상어 제외

                removeShark.extend(removeList) # 제거 목록에 추가
                    
        shark_ = []
        # 기존 상어에서 제거할 상어 인덱스 제외 -> 새로 상어 목록 생성
        for p in list(set( [x for x in range(len(self.shark))] ) - set(removeShark)):
            shark_.append( self.shark[p] ) # 인덱스를 통해 기존 상어 정보 입력
        self.shark = shark_[:] # 상어 목록 갱신
        
        return 

    # 현재 위치, 최대 길이, 속도, 방향 -> 최종 상어 위치, 방향 반환
    def moving(self, x, val, fast, dir):
        # 속도 = 이동 거리
        # 이동 거리가 0이 될때까지 반복
        while fast > 0: 
            if dir: # 방향이 True -> 오름차순
                if fast + x <= val:
                    x = x + fast
                    fast  = 0
                else:
                    fast -= (val - x)
                    x = val
                    dir = False # 방향 변경
            else: # 방향이 내림차순
                if x - fast > 0:
                    x -= fast
                    fast  = 0
                else:
                    fast -= (x-1)
                    x = 1
                    dir = True

        return x, dir

    # 상어 하나 이동 함수
    def sharkMove(self, shark):
        y, x, fast, direction, size = shark

        if direction == 1: # 위쪽
            y, change = self.moving(y, self.H, fast, False)
            if  change: direction = 2 # 벽에 닿으면 방향 변경

        elif direction == 2: # 아래쪽
            y, change = self.moving(y, self.H, fast, True)
            if  not change: direction = 1
        
        elif direction == 3: # 오른쪽
            x, change = self.moving(x, self.W, fast, True)
            if  not change: direction = 4
        
        else: # 왼쪽
            x, change = self.moving(x, self.W, fast, False)
            if  change: direction = 3

        return [y, x, fast, direction, size]

    # 상어 잡는 함수
    def catchShark(self):
        # 가장 가까운 상어 인덱스, 낚시왕과의 거리
        maxIndex, closer = -1, self.H+1 
        for index, shark in enumerate(self.shark):
            if shark[1] == self.man:  # x 축이 같으면
                if shark[0] < closer: # 기존 상어보다 더 가까우면
                    closer = shark[0] # closer 갱신
                    maxIndex = index # maxIndex 갱신
        
        if maxIndex != -1: # 값이 변하였으면
            # 잡은 상어 크기 추가
            self.sharkSize += self.shark[maxIndex][-1]
            # 잡은 상어 제거
            del self.shark[maxIndex]

        return


if __name__ == "__main__":
    R, C, M = map(int, input().split())
    shark = []
    for _ in range(M): shark.append( [ int(x) for x in input().split() ]  )
    # d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽
    # s는 속력, d는 이동 방향, z는 크기
    
    fishing = Fishing(R, C, M, shark) #클래스 선언

    for _ in range(C):
        # 낚시왕 이동
        fishing.man += 1
        # 상어 잡기
        fishing.catchShark()
        # 상어 이동
        fishing.sharkChange()

    print(fishing.sharkSize) # 최종, 잡은 상어 크기 합 출력
    

