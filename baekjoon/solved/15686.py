"""
Date : 21.04.19
Problems : https://www.acmicpc.net/problem/15686
Title : 치킨 배달
"""

class ChickenStreet:
    def __init__(self, N, M, city):
        self.N = N
        self.M = M
        self.city = city
        self.chickens = [] #현재 치킨집 위치
        for y in range(N):
            for x in range(N):
                # 최초 모든 치킨집 위치 입력
                if self.city[y][x] == 2: self.chickens.append( (y, x) )

    # 두 좌표 사이 거리 계산
    def calcDistance(self, y1, x1, y2, x2):
        return abs(y1-y2)+abs(x1-x2)

    # 하나의 집에 대한 치킨 거리 구하기
    def getHomeChicken(self, home_y, home_x):
        chickenStreet = 50 * 50
        for y, x in self.chickens :
            distance = self.calcDistance(home_y, home_x, y, x)
            # 치킨 거리가 제일 작은 것
            if chickenStreet > distance: chickenStreet = distance

        return chickenStreet

    # 도시의 치킨 거리 구하기
    def getCityChicken(self):
        sumCity = 0
        for y in range(self.N):
            for x in range(self.N):
                # 집에 대한 치킨 거리 더해줌
                if self.city[y][x] == 1:
                    sumCity += self.getHomeChicken(y, x)
        return sumCity

    # 치킨집 조합 계산
    def setCombination(self):
        chickenDict = {}
        for index, position in enumerate(self.chickens):
            chickenDict[index] = position # 딕셔너리 생성

        result = []
        combine = []
        def dfs(line): #DFS를 이용하여 조합 구하기
            if len(combine) == self.M: #최대 M개의 치킨집
                result.append(combine[:])
                return

            for i in line: 
                combine.append(i)
                index = line.index(i)
                newLine = line[index+1:]
                dfs(newLine)
                combine.pop()

            return

        dfs( list(chickenDict.keys()) )
        return chickenDict, result

if __name__ == "__main__":
    N, M = map(int, input().split())
    city = []
    for _ in range(N): city.append( [int(x) for x in input().split()] )

    chicken = ChickenStreet(N, M, city) # 클래스 선언
    chickenDict, combine = chicken.setCombination() # 치킨집 조합 구하기

    minChicken = 50 * 50
    for comb in combine: # 모든 조합 확인
        newChicken = []
        # 조합에 해당하는 치킨집 좌표 설정
        for c in comb: newChicken.append( chickenDict[c] )
        chicken.chickens = newChicken # 치킨집 좌표 재설정
        city_chicken = chicken.getCityChicken() # 도시 치킨 거리 계산
        if minChicken > city_chicken: # 최소 치킨 거리 구하기
            minChicken = city_chicken

    print(minChicken )


