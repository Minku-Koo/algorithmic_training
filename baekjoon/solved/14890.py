"""
Date : 21.10.20
Problems : https://www.acmicpc.net/problem/14890
Title : 경사로
"""
# BFS

def solution(n, l, box):
    result=0
    def checkOverWidth(l, line, checkLine, index, index2):
        if line[index]>line[index2]:
            for i in range(l):
                ni = index2+i
                if ni >= len(line): return 0, checkLine
                if checkLine[ni] == 1: return 0, checkLine
                
                if line[index2]!=line[ni]: return 0, checkLine
            for i in range(l):
                ni = index2+i
                checkLine[ni] = 1
            
        else:
            for i in range(l):
                ni = index-i
                if ni<0: return 0, checkLine
                if checkLine[ni] == 1: return 0, checkLine
                if line[index]!=line[ni]: return 0, checkLine
            for i in range(l):
                ni = index-i
                checkLine[ni] = 1
        
        return True, checkLine

    def isPossible( line):
        checkLine = [0]*len(line)
        if 1 == len(set(line)): return True
        for i, p in enumerate(line[:-1]):
            if line[i]==line[i+1]: continue
            check, checkLine = checkOverWidth(l, line, checkLine, i, i+1)
            if not check: return False
            if line[i]-line[i+1]>1 or line[i]-line[i+1]<-1:
                return False

        return True
    
    for  line in box:
        
        if isPossible(line): 
            result+=1
    
    for y in range(n):
        temp = []
        for x in range(n):
            temp.append(box[x][y])
        if isPossible(temp): 
            result+=1


    return result


if __name__ == "__main__":
    n, l = list(map(int, input().split()))
    box = []
    for _ in range(n):
        box.append(list(map(int, input().split())))
        
    print( solution(n, l, box) )



