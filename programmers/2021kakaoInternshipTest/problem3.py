# 21.05.08

def solution(n, k, cmd):
    line = {}
    for i in range(n): line[i] = str(i)
    resavers = []
    loc = k # 선택된 행
    answer = ''
    
    def ux(loc, x): # x만큼 위로 이동
        return loc - x
    def dx(loc, x): # x만큼 아래로 이동
        return loc+x
    
    def delCell(line, loc):
        delname = line[loc]
        delloc = loc
        
        for i in range(loc, len(line)-1):
            line[i] = line[i+1]
            
        line.pop( max(line.keys()) )
        # print("line len", len(line))
        # print("loc", loc)
        if loc > len(line) -1:
            print(line)
            loc = len(line)-1
            
        return (delloc, delname), line, loc
    
    def resave(line, loc, new):
        newloc, newname = new
        if newloc <= loc: loc += 1
        
        
        for i in range(len(line)-1, newloc-1, -1):
            line[i+1] = line[i]
            
        line[newloc] = newname
        return line, loc
    
    for order in cmd:
        print(order)
        if order == "C":
            dell, line, loc = delCell(line, loc)
            resavers.append( dell )
        elif order == "Z":
            new = resavers.pop()
            line, loc = resave(line, loc, new)
        elif order[0] == "D":
            loc = dx(loc, int(order[-1]))
        elif order[0] == "U":
            loc = ux(loc, int(order[-1]))
        print("line", line)
        print("loc", loc)
    
    saved = [int(line[x]) for x in line.keys()]
    for i in range(n):
        if i in saved:
            answer+="O"
        else:
            answer+="X"
    
    
    return answer