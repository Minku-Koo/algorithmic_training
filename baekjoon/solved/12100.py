"""
Date : 21.10.18
Problems : https://www.acmicpc.net/problem/12100
Title : 2048 (Easy)
"""
# BFS
def solution(size, box):
    
    def getMax(box): return max([max(i) for i in box])
    def isSame(box, newbox):
        for i, j in zip(box, newbox):
            if i!= j: return False
        return True

    def move(boxx, dir):
        box = [p[:] for p in boxx]
        size = len(box)
        newbox = [ [0]*size for _ in range(size) ]
        
        if dir=="u":
            # 위에서부터 인접한 같은 숫자는 합치기
            for i in range(size):
                line = []
                for j in range(size):
                    if box[j][i]!=0: line.append(box[j][i])
                for q in range(len(line)):
                    newbox[q][i] = line[q]
                    
        elif dir=="d":
            for i in range(size):
                line = []
               
                for j in range(size):
                    k = size - j - 1
                    if box[k][i]!=0: line.append(box[k][i])
                for q in range(len(line)):
                    newbox[size-1-q][i] = line[q]

        elif dir=="l":
            for i in range(size):
                line = []
                for j in range(size):
                    if box[i][j]!=0: line.append(box[i][j])
                for q in range(len(line)):
                    newbox[i][q] = line[q]

        elif dir=="r":
            for i in range(size):
                line = []
                
                for j in range(size):
                    k = size - j - 1
                    if box[i][k]!=0: line.append(box[i][k])
                for q in range(len(line)):
                    newbox[i][size-1-q] = line[q]
        return newbox

    def sumBox(boxx, dir):
        box = [p[:] for p in boxx]
        size = len(box)
        box = move(box, dir)
        if dir=="u":
            
            # 위에서부터 인접한 같은 숫자는 합치기
            for i in range(size):
                for j in range(size-1):
                    if box[j][i] == box[j+1][i]:
                        box[j][i] = box[j+1][i] *2
                        box[j+1][i] = 0
                        
            # 0을 모두 제외하고 위에서부터 정렬
        elif dir=="d":
            for i in range(size):
                for j in range(size-1):
                    k = size - j - 1
                    if box[k][i] == box[k-1][i]:
                        box[k][i] = box[k-1][i] *2
                        box[k-1][i] = 0
        elif dir=="l":
            for i in range(size):
                for j in range(size-1):
                    if box[i][j] == box[i][j+1]:
                        box[i][j] = box[i][j+1] *2
                        box[i][j+1] = 0
        
        elif dir=="r":
            for i in range(size):
                for j in range(size-1):
                    k = size - j - 1
                    if box[i][k] == box[i][k-1]:
                        box[i][k] = box[i][k-1] *2
                        box[i][k-1] = 0

        box = move(box, dir)
        return box

    def bfs():
        result = 0
        queue = [(0, box)]
        maxVal = 0
        while queue:
            count, bbox = queue.pop(0)
            orgb = [q[:] for q in bbox]
            if count==6: break
            for dir in ['r','l','u','d']:
                # 이동: newbox = move(bbox, dir)
                
                newbox = sumBox(bbox, dir)
                
                if not isSame(newbox, orgb):
                # 큐에 추가: queue.append( (count+1, newbox) )
                    queue.append( (count+1, newbox) )

                    if 5>count>3:
                        maxVal =  getMax(newbox)
                        if maxVal>result: 
                            result=maxVal
                        
        return result if result>0 else getMax(newbox)

    
    return bfs()


if __name__ == "__main__":
    size = int(input())
    box = []
    for _ in range(size): box.append(list(map(int, input().split())))

    print(solution(size, box))

