"""
Date : 21.04.23
Problems : https://www.acmicpc.net/problem/5373
Title : 연구소3
"""


class Laboratory:
    def __init__(self, n, m, lab):
        self.n, self.m = n ,m
        self.lab = lab
        self.virus, self.wall = [], []
        for y in range(n):
            for x in range(n):
                # if lab[y][x] == 1: self.wall.append( (y, x) )
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
        newLab = newLab[:]

        def bfs(combine, newLab, minVal):
            queue = []
            check = []
            for com in combine:
                queue.append( com )
                check.append( com )
                newLab[ com[0] ][com[1] ] = 1
            # for l in newLab: print(l)
            # print("**>"*20)
           
            while queue:
                y, x = queue.pop(0)
                # if y<0 or x<0 : return
                # if y>=self.n-1 or x>=self.n-1: return

                vir = newLab[y][x]

                y_, x_ = y-1, x
                if (y_, x_) not in check:
                # if y>0:
                    # y_, x_ = y-1, x
                    if y>0 and newLab[y_][x_] != -1 :#and newLab[y_][x_] != -2:
                        # if newLab[y_][x_] == -2: newLab[y_][x_] = vir +1
                        # else: 
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
                        newLab[y_][x_] = vir +1
                        queue.append( (y_, x_) )
                        check.append( (y_, x_) )

                        if vir >= minVal and (y_, x_) not in combine :
                            newLab[y_][x_] = minVal * minVal
                            break 

                if x>0:
                    y_, x_ = y, x-1
                    if (y_, x_) not in check and newLab[y_][x_] != -1 :#and newLab[y_][x_] != -2:
                        # if newLab[y_][x_] == -2: newLab[y_][x_] = vir +1
                        # else: 
                        newLab[y_][x_] = vir +1
                        queue.append( (y_, x_) )
                        check.append( (y_, x_) )

                        if vir >= minVal and (y_, x_) not in combine :
                            newLab[y_][x_] = minVal * minVal
                            break 
                
                if x<self.n-1:
                    y_, x_ = y, x+1
                    if (y_, x_) not in check and newLab[y_][x_] != -1 :#and newLab[y_][x_] != -2:
                        # if newLab[y_][x_] == -2: newLab[y_][x_] = vir +1
                        # else: 
                        #     newLab[y_][x_] = vir +1
                        newLab[y_][x_] = vir +1
                        queue.append( (y_, x_) )
                        check.append( (y_, x_) )

                        if vir >= minVal and (y_, x_) not in combine :
                            newLab[y_][x_] = minVal * minVal
                            break 
                
            newLab = self.clearLab(combine, newLab)
            
            return 


        bfs(combine, newLab[:], minVal)
        
        return newLab
            
def getSum(lab):
    result = []
    for l in lab:
        if 0 in l: return 0
        else: result.append( max(l) )

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
        newlaboratory = [ [x for x in a] for a in newLab ]
        
        virus_lab = laboratory.expandVirus(comb, newlaboratory, minVal)
        
        sumLab = getSum(virus_lab)
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



