"""
Date : 21.04.19
Problems : https://www.acmicpc.net/problem/16236
Title : 아기 상어 
"""

class BabyShark:
    def __init__(self, N, maps):
        self.N = N
        self.map = maps
        self.eat = 0 # 아기 상어 물고기 먹은 횟수
        self.move = 0 # 아기 상어 이동 횟수
        self.sharkSize = 2 # 최초 아기 상어 크기
        # 아기 상어 최초 위치
        for y in range(N):
            for x in range(N):
                if maps[y][x] == 9:
                    self.x,self.y = x, y
                    # 현재 상어 위치 0 입력
                    self.map[y][x] = 0 
                    break
    
    # 먹을 수 있는 물고기 여부 판단
    # False -> 더이상 못먹음 -> 도움 요청
    def canEatFish(self):
        minFish = 100 #물고기 크기 100으로 초기화
        for y in range(self.N):
            for x in range(self.N):
                if self.map[y][x] == 0: continue # 0 제외
                if minFish > self.map[y][x]: minFish = self.map[y][x]
            # 먹을 물고기가 있으면
            if minFish < self.sharkSize: return True
        # 변한 것이 없으면
        if minFish == 100: return False
        # 최대 물고기 크기보다 상어 크기가 작으면
        if minFish >= self.sharkSize: return False
        else: return True
    
    # 현재 상어 위치 <-> 해당 물고기 간 거리 계산
    # BFS 이용하여 계산
    def calcDistance(self, root, y_, x_):
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        check = []
        # map과 같은 크기로 check 설정 (0으로 채움)
        for x in self.map: check.append( [ 0 for _ in x] )
        queue = [root] # 큐에 상어 위치 추가

        while queue: # 큐가 빌 때 까지 반복
            y , x = queue.pop(0) # 큐에서 꺼내옴
            
            if y_==y and x_ == x: # 물고기를 만나면
                return check[y_][x_] # 최단거리 반환

            for i in range(4): # 상하좌우 확인
                nx = x + dx[i]
                ny = y + dy[i]
                # 바깥으로 벗어나지 않고
                if 0 <= nx < self.N and 0 <= ny < self.N:
                    if check[ny][nx] == 0 : 
                        # 상어가 먹을 수 있는 물고기 크기일 경우
                        if self.map[ny][nx] <= self.sharkSize:
                            check[ny][nx] = check[y][x] + 1
                            queue.append((ny,nx))
        
        return -1 # 물고기를 만날 수 없는 경우

    # 먹을 수 있는 물고기 중 가장 가까운 물고기 계산
    def checkFish(self):
        fishs = []
        for y in range(self.N):
            for x in range(self.N):
                # 먹을 수 있는 물고기라면
                if 0 < self.map[y][x] < self.sharkSize:
                    fishs.append( (y, x) )

                    # 물고기와 상어가 바로 옆에 있는 경우
                    if self.y == y or self.x == x: 
                        if abs(self.y-y)+abs(self.x-x) == 1: 
                            return [y, x], 1 # 물고기 위치 반환

        minDistance = 20 * 20 # 이동 최대값으로 초기화
        pointList = [] # 물고기 위치 리스트
        # 좌표 기준으로 오름차순 정렬
        for y, x in sorted(fishs, key=lambda x:( x[0] , x[1] ) ):
            distance = self.calcDistance((self.y, self.x), y, x)
            
            if distance != -1: #오류가 없는 경우
                if distance <= minDistance: # 기존 거리보다 작거나 같으면
                    if distance < minDistance: # 작을 경우
                        minDistance = distance # 최단 거리 초기화
                        pointList = [(y, x)] # 물고기 위치 초기화
                    else: pointList.append((y, x)) # 같을 경우 -> 추가
        # 만날 수 있는 물고기가 없으면 -> 물고기 좌표 반환, 거리 = 0
        if pointList == []: return (y, x),0
        # 만날 수 있는 최단거리 물고기 중에서 우선순위 고려하여 반환
        return sorted(pointList, key=lambda x:(x[0], x[1]) )[0]  , minDistance
        
    # 상어 이동
    # 물고기 위치, 거리, 에러 여부
    def moveShark(self, point, distance, err = False):
        temp = (self.y, self.x) # 현재 상어 위치 임시 저장
        self.y, self.x = point # 상어 위치를 물고기 위치로 변경
        self.eat += 1 # 먹은 횟수 추가
        self.move += distance # 이동 거리 추가
        self.map[self.y][self.x] = 0 # 해당 물고기 자리 0으로 설정
        if err: # 에러 있으면
            self.y, self.x = temp # 다시 상어 제자리
            self.eat -= 1 # 먹은 횟수 차감

        if self.sharkSize == self.eat: # 상어가 자신 크기만큼 먹었으면
            self.sharkSize += 1 # 상어 크기 증가
            self.eat = 0 # 먹은 횟수 초기화

        return

if __name__ == "__main__":
    N = int(input())
    maps = []
    for _ in range(N): maps.append( [int(x) for x in input().split()] )
    
    baby_shark = BabyShark(N, maps) # 클래스 선언
    
    while baby_shark.canEatFish(): # 먹을 수 있는 물고기가 있으면
        point, distance = baby_shark.checkFish() # 최단거리 물고기 위치, 거리 계산
        err = False
        if distance == 0: err = True # 거리 = 0 --> 에러
        baby_shark.moveShark(point, distance, err) # 상어 이동
    print(baby_shark.move) # 이동 횟수 ()= 이동 시간) 출력

    '''
    # 반례 확인할 수 있는 곳
    # https://www.acmicpc.net/board/view/49232
    # https://www.acmicpc.net/board/view/56644

    '''
