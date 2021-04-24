"""
Date : 21.04.24
Problems : https://www.acmicpc.net/problem/17142
Title : 연구소3
"""


class Laboratory:
    def __init__(self, n, m, lab):
        self.n, self.m = n ,m
        self.lab = lab
        self.virus, self.wall = [], []
        for y in range(n):
            for x in range(n):
                if lab[y][x] == 2: self.virus.append( (y, x) )

    # 바이러스 조합 구하기
    def virusCombine(self):
        result = []
        check = []
        def dfs(line):
            if len(check) == self.m:
                result.append(check[:])
                return

            for w in line:
                index = line.index(w)
                newLine = line[index+1:]
                check.append(w)
                dfs(newLine)
                check.pop()

            return
        
        dfs(self.virus[:])

        return result

    def getNewLab(self):
        newLab = []
        for line in self.lab:
            temp = []
            for c in line:
                if c == 1: # 벽
                    temp.append( -1 )
                elif c == 2: # 바이러스
                    temp.append( -2 )
                else:
                    temp.append( 0 )
            newLab.append( temp)
        return newLab
    
    def clearLab(self, comb, lab):
        for y, x in self.virus:
            if (y, x) not in comb:
                lab[y][x] = -2
        
        return lab
    
    # 바이러스 퍼지는 시간 구하기
    def expandVirus(self, combine, newLab, minVal):
        # newLab = newLab[:]

        def bfs(combine, newLab, minVal):
            queue = []
            check = []
            for com in combine:
                queue.append( com )
                check.append( com )
                newLab[ com[0] ][com[1] ] = 1
            # for l in newLab: print(l)
            # print("**>"*20)
            plus = [[-1,1,0,0] ,[0,0,-1,1]]
            isout = False
            cont = 1
            while queue:
                cont += 1
                y, x = queue.pop(0)
                vir = newLab[y][x]
                # check = list(set(check))
                # y_, x_ = y-1, x
                # if (y_, x_) not in check:
                for i in range(4):
                    y_, x_ = y + plus[0][i], x + plus[1][i]
                    if y_<0 or x_<0 or x_>self.n-1 or y_>self.n-1: continue
                    if (y_, x_) not in check and (newLab[y_][x_] == 0 or newLab[y_][x_] == -2) :
                        queue.append( (y_, x_) )
                        check.append( (y_, x_) )
                        newLab[y_][x_] = 2

                        if cont >= minVal : #and (y_, x_) not in combine :
                            newLab[y_][x_] = minVal * minVal
                            isout = True
                            break 
                if isout: break
                '''
                if y>0:
                    y_, x_ = y-1, x
                    if (y_, x_) not in check and newLab[y_][x_] != -1 :#and newLab[y_][x_] != -2:
                        # if newLab[y_][x_] == -2: newLab[y_][x_] = vir +1
                        # else: 
                        # if newLab[y_][x_] ==0 or newLab[y_][x_] ==-2 :
                        queue.append( (y_, x_) )
                        check.append( (y_, x_) )
                        newLab[y_][x_] = vir +1

                        if vir >= minVal and (y_, x_) not in combine :
                            newLab[y_][x_] = minVal * minVal
                            break 
                        
                
                if y<self.n-1:
                    y_, x_ = y+1, x
                    if (y_, x_) not in check and newLab[y_][x_] != -1 :#and newLab[y_][x_] != -2:
                        # if newLab[y_][x_] == -2: newLab[y_][x_] = vir +1
                        # else: 
                        
                        # if newLab[y_][x_] ==0 or newLab[y_][x_] ==-2 :
                        queue.append( (y_, x_) )
                        check.append( (y_, x_) )
                        newLab[y_][x_] = vir +1
                        if vir >= minVal and (y_, x_) not in combine :
                            newLab[y_][x_] = minVal * minVal
                            break 

                if x>0:
                    y_, x_ = y, x-1
                    if (y_, x_) not in check and newLab[y_][x_] != -1 :#and newLab[y_][x_] != -2:
                        # if newLab[y_][x_] == -2: newLab[y_][x_] = vir +1
                        # else: 
                        
                        # if newLab[y_][x_] ==0 or newLab[y_][x_] ==-2 :
                        queue.append( (y_, x_) )
                        check.append( (y_, x_) )
                        newLab[y_][x_] = vir +1
                        if vir >= minVal and (y_, x_) not in combine :
                            newLab[y_][x_] = minVal * minVal
                            break 
                
                if x<self.n-1:
                    y_, x_ = y, x+1
                    if (y_, x_) not in check and newLab[y_][x_] != -1 :#and newLab[y_][x_] != -2:
                        # if newLab[y_][x_] == -2: newLab[y_][x_] = vir +1
                        # else: 
                        #     newLab[y_][x_] = vir +1
                        
                        # if newLab[y_][x_] ==0 or newLab[y_][x_] ==-2 :
                        queue.append( (y_, x_) )
                        check.append( (y_, x_) )
                        newLab[y_][x_] = vir +1
                        if vir >= minVal and (y_, x_) not in combine :
                            newLab[y_][x_] = minVal * minVal
                            break 
                '''
            # newLab = self.clearLab(combine, newLab)
            
            return cont


        count  = bfs(combine, newLab, minVal)
        
        return count  #newLab
            
def getSum(lab):
    result = []
    for l in lab:
        if 0 in l: return 0
        result.append( max(l) )

    return max(result)


if __name__ == "__main__":
    n, m = map(int, input().split())
    lab = []
    for _ in range(n): lab.append( list(map(int, input().split())) )

    import time
    
    laboratory = Laboratory(n, m, lab)
    virus_combine = laboratory.virusCombine()
    newLab = laboratory.getNewLab()

    minVal = 50 * 50
    exp = time.time()
    for comb in virus_combine:
        # print("virus loc", comb)
        # newlaboratory = [ a[:] for a in newLab ]
        
        sumLab = laboratory.expandVirus(comb, newLab, minVal)
        # sumLab = getSum(virus_lab)
        
        # sumLab = getSum( laboratory.expandVirus(comb, newLab, minVal) )
        if sumLab == 0: continue
        # if minVal < 100: print(minVal)
        if minVal > sumLab:
            print(sumLab)
            minVal = sumLab

    if minVal ==  50 * 50:
        minVal = 0
        # if minVal > virus_lab:
        #     minVal = virus_lab
    print("exp time", time.time()-exp)
    print(minVal-1 )



