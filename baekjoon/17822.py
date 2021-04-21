"""
Date : 21.04.21
Problems : https://www.acmicpc.net/problem/17822
Title : 원판 돌리기
"""

class Circle:
    def __init__(self, N, M, T, maps, orders ):
        self.N, self.M, self.T = N, M, T
        self.map = maps
        self.order = orders

    # x번째 판 회전해주는 함수
    def moving(self, x, d, k):
        # print("x", x)
        new_map = self.map[:][x-1]
        if d == 0: #시계방향
            for _ in range(k):
                temp = new_map.pop()
                new_map.insert(0, temp)
        else: #반시계 방향
            # new_map = new_map[k:] + new_map[:k]
            for _ in range(k):
                temp = new_map.pop(0)
                new_map.append(temp)
        self.map[x-1] = new_map
        return

    # 인접 숫자 지우기
    def eraseNum(self):
        # print(">> do erase")
        result = []
        check = []
        
        def dfs(y, x,  before = 0, dir=0):
            # if 0>y or y>self.N-1: return
            # if 0>x or x>self.M-1: return
            # if len(check)>100: return check
            
            number = self.map[y][x]
            # print(y, x, number)
            
            if number == 0: return
            if (y, x) in check: return
            if number != before: return
            
            
            check.append((y, x))
            # print("erase num:", y, x)
            # self.map[y][x] = 0
            if dir!=2 and y<self.N -1 :
                dfs(y+1, x,  before = number, dir=1)
            if dir!=1 and y>0 :
                dfs(y-1, x,  before = number, dir=2)
            if dir!=4 and x<self.M-1 :
                dfs(y, x+1, before = number, dir=3)
            if dir!=3 and x >0 :
                dfs(y, x-1,  before = number, dir=4)


            return check

        def sameNum():
            sameNumbers = []
            for y in range(len(self.map)):
                for x in range(len(self.map[0])):
                    number = self.map[y][x]
                    if number == 0: continue
                    # 이미 들어가있는지 체크할 필요?
                    if  y<self.N -1 :
                        if self.map[y+1][x] == number:
                            sameNumbers.append( (y+1, x) )
                    if  y>0 :
                        if self.map[y-1][x] == number:
                            sameNumbers.append( (y-1, x) )

                    if  x>0 :
                        if self.map[y][x-1] == number:
                            sameNumbers.append( (y, x-1) )

                        if x==self.M-1:
                            if self.map[y][0] == number:
                                sameNumbers.append( (y, 0) )

                    if  x<self.M-1 :
                        if self.map[y][x+1] == number:
                            sameNumbers.append( (y, x+1) )

                        if x==0:
                            if self.map[y][self.M-1] == number:
                                sameNumbers.append( (y, self.M-1) )

            return list(set(sameNumbers))
                    

        ischange = False
        # newMap = [ [x for x in line] for line in self.map]
        newMap = [ line[:] for line in self.map]

        # DFS 말고, 가로 전부 비교 + 새로 전부 비교로 변경
        # 새로운 맵 생성해서, 기존 맵 + 뉴 맵에 이제 0 채워넣고 나중에 기존 맵에 복사
        '''
        for y in range(self.N):
            for x in range(self.M):
                # print("y",y,"/ x", x, "bef",self.map[y][x])
                numb = self.map[y][x]
                if numb==0: continue
                # import time
                # st = time.time()

                same = dfs(y, x, before =numb)
                # same = sameNum()


                # print("dfs time", time.time()-st)
                if same == None: same = []
                if x == 0:# and self.map[y][x]!=0:
                    if numb == self.map[y][-1]:
                        same.append( (y, self.M-1) )
                        same.append( (y, 0) )
                if x == self.M-1:# and self.map[y][x]!=0:
                    if numb == self.map[y][0]:
                        same.append( (y, 0) )
                        same.append( (y, self.M-1) )
                # if same != []:print("same", same)
                if  len(same)>1:
                    ischange = True
                    for i,j in same: 
                        # self.map[i][j] = 0
                        newMap[i][j] = 0
                    
                check = []
        '''
        same = sameNum()
        if same == None: same = []
        if  len(same)>1:
            ischange = True
            for i,j in same: 
                self.map[i][j] = 0
        
        if not ischange:
            sumMap = 0
            count = 0
            for line in self.map: 
                count += self.M - line.count(0)
                sumMap += sum(line)

            if sumMap ==0: average = 0
            else: average = sumMap / count

            for y in range(self.N):
                for x in range(self.M):
                    number = self.map[y][x]
                    if number == 0: continue
                    if number < average:
                        self.map[y][x] += 1
                    elif number > average:
                        self.map[y][x] -= 1
                        
        return 


if __name__ == "__main__":
    N, M, T = list(map(int, input().split()))
    maps = []
    for _ in range(N): maps.append(list(map(int, input().split())))
    orders = []
    for _ in range(T): orders.append(list(map(int, input().split())))

    circle = Circle(N, M, T, maps, orders)
    
    for x, d, k in orders:
        max_ = N // x
        for m in range(1, max_+1):
            circle.moving(x*m, d, k)
        circle.eraseNum()
        
    
    result = 0
    for j in circle.map: result += sum(j) 
    print(result)
    
    