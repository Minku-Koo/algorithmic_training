"""
Date : 21.04.20
Problems : https://www.acmicpc.net/problem/15684
Title : 사다리 조작
"""

# 시간 초과 문제 미해결

class Ladder:
    def __init__(self, N, M, H, ladders):
        self.N = N
        self.M = M
        self.H = H
        self.ladder = ladders

    # x 번째에서 출발하면 몇 번째에 도착할까?
    def ladderDown(self, x, new_ladder):
        p = [1, x] #출발 위치

        start = 0
        new_ladder = sorted(new_ladder)
        for h in range(self.H):
            start = 0
            # new_ladder = sorted(new_ladder,key=lambda x:(x[0],x[1]))
            for i, ld in enumerate(new_ladder):
                if p[0] != ld[0]:
                    if p[0] > ld[0]: continue
                    if p[0] < ld[0]:  break
                    
                start = i
                # 가로선 좌측과 만나면
                ch = ld[1]
                # if ld == p:  
                if ch == p[1]:  
                    p[1] = ld[1] + 1
                    # if abs(p[1]-x)>self.H - p[0]: return x+1
                    break
                # 가로선 우측과 만나면
                elif  p[1] - 1 == ch:
                # elif  p[1] - 1 == ld[1]:
                    p[1] = ld[1] 
                    # if abs(p[1]-x)>self.H - p[0]: return x+1
                    break
                # gap = self.H - p[0]
                # if abs(p[1]-x)>gap: return x+1
            # new_ladder = new_ladder[start: ]
            new_ladder = new_ladder[start: ]
            
            p[0] += 1
        
        return p[1]

    # 조건 만족하는가? 모든 세로선이 같은 번호로 끝나는가
    def checkPossible(self, new_ladder):
        # import time
        # k = time.time()
        for x in range(1, self.N+1):
            if x != self.ladderDown(x, new_ladder): 
                # print(x,">>",time.time()-k)
                return False
        
        return True

    # 놓을 수 있는 사다리 위치 구하기
    def addLadder(self):
        addPossible = []

        for y in range(1, self.H + 1):
            for x in range(1, self.N ):

                if [y, x] not in self.ladder and\
                [y, x+1] not in self.ladder and\
                [y, x-1] not in self.ladder: 
                    addPossible.append( [y, x] )

        return addPossible

    # 사다리 조합 구하기
    def getCombine(self, ladder, n):
        result = []
        check = []
        ispossible = [False]
        # if n == 1: 
        #     return  [ [x] for x in ladder ]
        # if n == 0: return [[]]
        # count = [0]
        def dfs(lines):
            # count[0] += 1
            if len(check) == n:
                # result.append(check[:])
                if self.checkPossible(self.ladder + check[:]):
                    # print("true--")
                    ispossible[0] = True
                    return True
                # print("output")
                # yield check[:]
                return False

            for w in lines[:]:
                index = lines.index(w)
                if  n > 1 and len(check)>0:
                    if check[-1][0] == w[0] or check[0][0] == w[0]:
                        if abs( check[-1][-1] - w[-1]) == 1: continue
                        if abs( check[0][-1] - w[-1]) == 1: continue
                    if check[-1][1] == w[1] or check[0][1] == w[1]:
                        if abs( check[-1][0] - w[0]) == 1: continue
                        if abs( check[0][0] - w[0]) == 1: continue
                check.append(w)
                newLine = lines[index+1:]
               
                if dfs(newLine): return True
                
                check.pop()
            return False

        # import time
        # tt = time.time()
        # print(num, "get combine start")
        dfs(ladder)
        # for d in dfs(ladder):
            # yield d
        # if num>1:
        #     print(num, "comb", time.time()-tt)
            # print("result count:", len(result))
        # print(num, count[0])
        if not ispossible[0]: return False
        return True
        # return sorted(result)



if __name__ == "__main__":
    N, M, H = list(map(int, input().split()))
    ladders = []
    for _ in range(M): ladders.append(list(map(int, input().split())))

    ladder = Ladder(N, M, H, ladders)

    # import time
    ##
    result = -1
    add_ladder = ladder.addLadder()
    for num in range(4):
        # st = time.time()
        # print(num, ladder.getCombine( add_ladder[:], num))
        if ladder.getCombine( add_ladder[:], num):
            result = num
            # print(num,"check possible>", time.time()-st)
            break
        # for add in ladder.getCombine( add_ladder[:], num):
        #     if ladder.checkPossible(ladder.ladder + list(add)):
        #         result = num
        #         break
        # print(num,"check possible fail>", time.time()-st)
        if result != -1: break
        
    print(result)
'''
10 5 30
1 3
3 2
4 7
5 5
9 5
>3
'''
