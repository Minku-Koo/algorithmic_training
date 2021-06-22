# 21.05.09

def solution(maps, p, r):
    answer = 0
    power = p
    rad = r
    
    def isinner(y, x):
        if y<0 or x<0 : return False
        if y>len(maps)-1 or x>len(maps)-1 : return False
        return True
    
    def getouts(outs, inners):
        result = []
        check = outs + inners
        while outs:
            y, x = outs.pop(0)
            
            y_, x_ = y-1, x
            if isinner(y_, x_) and (y_, x_) not in check:
                check.append( (y_, x_) )
                result.append( (y_, x_) )
            y_, x_ = y+1, x
            if isinner(y_, x_) and (y_, x_) not in check:
                check.append( (y_, x_) )
                result.append( (y_, x_) )
            y_, x_ = y, x+1
            if isinner(y_, x_) and (y_, x_) not in check:
                check.append( (y_, x_) )
                result.append( (y_, x_) )
            y_, x_ = y, x-1
            if isinner(y_, x_) and (y_, x_) not in check:
                check.append( (y_, x_) )
                result.append( (y_, x_) )
            
        return result, check # 각각 outs, 전체
            
    
    def getall(y, x, step):
        inners = []
        outs = []
        
        #초기 1단계
        y_, x_ = y-2, x-2
        if isinner(y_, x_): outs.append( (y_, x_) )
        y_, x_ = y-2, x-1
        if isinner(y_, x_): outs.append( (y_, x_) )
        y_, x_ = y-1, x-2
        if isinner(y_, x_): outs.append( (y_, x_) )
        y_, x_ = y-1, x-1
        if isinner(y_, x_): outs.append( (y_, x_) )
        
        if step ==1: return inners, outs
            
        for _ in range(step-1):
            outs, alls = getouts(outs, inners)
            inners = list(set(alls) - set(outs))
            
        return outs, inners
    
    def killing(out, inn):
        result = 0
        for y, x in out:
            if maps[y][x] <= power / 2:
                result += 1
        for y, x in inn:
            if maps[y][x] <= power :
                result += 1
        return result
    
    # 모든 셀 확인
    maxkill = 0
    for i in range(1, len(maps)+2):
        for j in range(1, len(maps)+2):
            outs, inners = getall(i, j, rad//2)
            killcount = killing(outs, inners)
            if killcount > maxkill:
                maxkill = killcount
    answer = maxkill
    return answer
