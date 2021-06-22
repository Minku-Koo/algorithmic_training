# 21.05.08


def solution(places):
    answer = []
    
    
    def bfs(y, x, p):
        queue = [(y, x)]
        check = []
        dist = 0
        
        while queue:
            y, x = queue.pop()
            check.append((y, x))
            
            if y>0 :
                y_, x_ = y-1, x
                if (y_, x_) not in check and p[y_][x_] !="X":
                    if p[y_][x_] == "P" and dist <2:
                        return False
                    queue.append((y_, x_))
                    
            if x>0 :
                y_, x_ = y, x-1
                if (y_, x_) not in check and p[y_][x_] !="X":
                    if p[y_][x_] == "P" and dist <2:
                        return False
                    queue.append((y_, x_))
                    
            if x<4 :
                y_, x_ = y, x+1
                if (y_, x_) not in check and p[y_][x_] !="X":
                    if p[y_][x_] == "P" and dist <2:
                        return False
                    queue.append((y_, x_))
                    
            if y<4 :
                y_, x_ = y+1, x
                if (y_, x_) not in check and p[y_][x_] !="X":
                    if p[y_][x_] == "P" and dist <2:
                        return False
                    queue.append((y_, x_))
                    
            dist += 1
        return True
    
    def checking(plc):
        for y in range(5):
            for x in range(5):
                if plc[y][x] == "P":
                    if not bfs(y, x, plc):
                        return 0
        return 1
            
            
    for pl in places: # 대기실 하나씩
        answer.append( checking(pl) )
    
    return answer

