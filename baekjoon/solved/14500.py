"""
Date : 21.04.18
Problems : https://www.acmicpc.net/problem/14500
Title : 테트로미노
"""
#DFS
# Python3로 실행 시, 시간 초과로 실패
## PyPy3로 실행 시, 성공

class Tetromino:
    def __init__(self, maps):
        self.map = maps # 지도

    def getMax(self, N, M): # 최대값 구해주는 함수
        max_ = [0] #최대값 초기 설정
        def dfs(y, x, box=[], dir=0): # DFS 이용하여 경우의 수 계산
            # y, x : y, x 좌표
            # box : tetromino 집합
            # dir : 움직인 방향 (direction)
            if len(box) == 4: # 4개가 모이면
                if max_[0] < sum(box[:]): # 최대값과 비교
                    max_[0] = sum(box[:])
                return
            if y <0 or y>N-1 or x<0 or x>M-1 : # 지도 밖으로 이탈
                return
            
            box.append(self.map[y][x]) # tetromino 추가
            if dir!=1: #왔던 방향이 아니면
                dfs(y+1, x, box= box[:], dir=0) # 하
            if dir!=0:
                dfs(y-1, x, box= box[:], dir=1) # 상
            if dir!=3:
                dfs(y, x+1, box= box[:], dir=2) # 우
            if dir!=2:
                dfs(y, x-1, box= box[:], dir=3) # 좌

            return
        
        for i in range(N):
            for j in range(M):
                # 모든 element에 대해 최대값 계산
                dfs(i, j, [], [])
        
        maxVal = max_[0] # 기존 최대값

        # 요철(ㅗ, ㅓ, ㅜ, ㅏ) 모양 계산
        for y in range(N):
            for x in range(M):
                if y==0 or x==0 or y==N-1 or x==M-1: #시간 단축 위한 조건
                    # 4개의 모서리일 경우 -> 건너뜀
                    if (y ==0 and  x==0) or \
                    (y==N-1 and x==M-1)  or \
                    (y==0 and x==M-1)  or \
                    (y==N-1 and x==0) : continue
                
                # 현재 값 (중앙값)
                mapVal = self.map[y][x] 

                # 가장자리 element가 아닐 경우 (시간 단축 위한 조건)
                if y>0 and x>0 and x<M-1 and y<N-1:
                    # 상하좌우 3개 element 합중 최대값
                    val = mapVal+ max([
                                    self.map[y-1][x] + self.map[y-1][x-1] + self.map[y-1][x+1],
                                    self.map[y+1][x] + self.map[y+1][x-1] + self.map[y+1][x+1],
                                    self.map[y][x-1] + self.map[y+1][x-1] + self.map[y-1][x-1],
                                    self.map[y][x+1] + self.map[y+1][x+1] + self.map[y-1][x+1]
                                    ])
                    if maxVal < val: maxVal = val
                else:
                    if y !=0 and x>0 and x<M-1: #상
                        val = mapVal+ self.map[y-1][x] + self.map[y-1][x-1] + self.map[y-1][x+1]
                        if maxVal < val: maxVal = val
                    if y != N-1 and x>0 and x<M-1: #하
                        val = mapVal + self.map[y+1][x] + self.map[y+1][x-1] + self.map[y+1][x+1]
                        if maxVal < val: maxVal = val
                    if x != 0 and y>0 and y<N-1: #좌
                        val = mapVal + self.map[y][x-1] + self.map[y+1][x-1] + self.map[y-1][x-1]
                        if maxVal < val: maxVal = val
                    if x != M-1 and y>0 and y<N-1: #우
                        val = mapVal + self.map[y][x+1] + self.map[y+1][x+1] + self.map[y-1][x+1]
                        if maxVal < val: maxVal = val
        return maxVal

if __name__ == "__main__":
    N, M = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append( [i for i in map(int, input().split())] )
    
    t = Tetromino( maps) # 클래스 선언
    result = t.getMax(N, M) # 최대값 계산
    print(result)

