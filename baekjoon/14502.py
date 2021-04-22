"""
Date : 21.04.23
Problems : https://www.acmicpc.net/problem/14502
Title : 연구소
"""

class Laboratory:
    def __init__(self, n, m, lab):
        self.n, self.m = n, m
        self.lab = lab
        self.empty, self.virus = [], []
        for y in range(self.n):
            for x in range(self.m):
                if self.lab[y][x] == 0: self.empty.append((y, x))
                elif self.lab[y][x] == 2: self.virus.append((y, x))

    # 조합 생성
    def combine(self):
        result = []
        check = []

        def dfs(line):
            if len(check) == 3:
                result.append(check[:])
                return

            for w in line:
                start = line.index(w)
                check.append(w)
                new_line = line[start + 1:]
                dfs(new_line)
                check.pop()

            return

        dfs(self.empty[:])

        return result

    # 벽 세우기
    def makeWall(self, combine):
        newLab = [x[:] for x in self.lab]
        for loc in combine:
            y, x = loc
            newLab[y][x] = 1
        
        return newLab

    # 바이러스 확산'
    def expandVirus(self, newLab):
        
        def bfs(y, x):
            check = []
            queue = [(y, x)]

            while queue:
                y, x = queue.pop(0)
                newLab[y][x] = 2
                if y>0 :
                    y_, x_ = y-1, x
                    if newLab[y_][x_]  == 0:
                        if (y_, x_) not in check :
                            check.append((y_, x_))
                            queue.append((y_, x_))

                if y<self.n-1:
                    y_, x_ = y+1, x
                    if newLab[y_][x_] == 0:
                        if (y_, x_) not in check:
                            check.append((y_, x_))
                            queue.append((y_, x_))

                if x<self.m-1:
                    y_, x_ = y, x+1
                    if newLab[y_][x_] == 0:
                        if (y_, x_) not in check :
                            check.append((y_, x_))
                            queue.append((y_, x_))

                if x>0:
                    y_, x_ = y, x-1
                    if newLab[y_][x_] == 0:
                        if (y_, x_) not in check :
                            check.append((y_, x_))
                            queue.append((y_, x_))

            return

        
        
        for virus in self.virus:
            y, x = virus
            bfs(y, x)
        
        return newLab

    # 0 개수 확인
    def countZero(self, lab):
        result = 0
        for line in lab:result += line.count(0)
        return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    lab = []
    for _ in range(n): lab.append( list( map(int, input().split()) ) )

    lab = Laboratory(n, m, lab)
    comb = lab.combine()
    maxVal = 0
    
    for walls in comb:
        wallLab = lab.makeWall(walls)
        newLab = lab.expandVirus(wallLab)
        result = lab.countZero(newLab)
        if maxVal < result: maxVal = result
        
    print(maxVal)
