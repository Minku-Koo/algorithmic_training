"""
Date : 21.04.24
Problems : https://www.acmicpc.net/problem/17142
Title : 연구소3
"""

# 시간 초과 문제 미해결

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
        
        def bfs(combine, newLab, minVal):
            queue = []
            check = []
            for com in combine:
                queue.append( com )
                check.append( com )
                newLab[ com[0] ][com[1] ] = 2
                
            plus = [[-1,1,0,0] ,[0,0,-1,1]]
            isout = False
            cont = 0
            while queue:
                cont += 1
                y, x = queue.pop(0)
                vir = newLab[y][x]
                for i in range(4):
                    y_, x_ = y + plus[0][i], x + plus[1][i]
                    if y_<0 or x_<0 or x_>self.n-1 or y_>self.n-1: continue
                    if (y_, x_) not in check and (newLab[y_][x_] == 0 or newLab[y_][x_] == -2) :
                        queue.append( (y_, x_) )
                        check.append( (y_, x_) )
                        newLab[y_][x_] = 2

                        if cont >= minVal : 
                            newLab[y_][x_] = minVal * minVal
                            isout = True
                            break 
                if isout: break
                
            
            return cont


        count  = bfs(combine, newLab, minVal)
        
        return count  
            
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


    laboratory = Laboratory(n, m, lab)
    virus_combine = laboratory.virusCombine()
    newLab = laboratory.getNewLab()

    minVal = 50 * 50
    
    for comb in virus_combine:
        
        sumLab = laboratory.expandVirus(comb, newLab, minVal)
        
        if sumLab == 0: continue
        
        if minVal > sumLab:
            print(sumLab)
            minVal = sumLab

    if minVal ==  50 * 50:
        minVal = 0
        
        
    print(minVal-1 )



