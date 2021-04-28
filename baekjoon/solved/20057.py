"""
Date : 21.04.24
Problems : https://www.acmicpc.net/problem/20057
Title : 마법사 상어와 토네이도
"""

n = int(input())
maps = []
for _ in range(n): maps.append( list(map(int, input().split())) )


def isout(y, x):
    global n
    if y<0 or x<0 or y>n-1 or x>n-1: return True
    return False

# 모래 날리는 함수
def tornaido(y, x, dir, maps):
    
    solid = maps[y][x]
    if solid ==0: return maps, 0
    out = 0
    less = 0
    maps[y][x] = 0
    if dir in [1, 2]: # 상
        
        mount = int( solid * 0.07 )
        less += mount*2
        if isout(y, x+1): out += mount
        else: maps[y][x+1] += mount 
        if isout(y, x-1): out += mount
        else: maps[y][x-1] += mount 

        mount = int( solid * 0.02 )
        less += mount*2
        if isout(y, x-2): out += mount
        else: maps[y][x-2] += mount 
        if isout(y, x+2): out += mount
        else: maps[y][x+2] += mount 

        if dir == 1:
            mount = int( solid * 0.1 )
            less += mount*2
            if isout(y-1, x-1): out += mount
            else: maps[y-1][x-1] += mount 
            if isout(y-1, x+1): out += mount
            else: maps[y-1][x+1] += mount 

            mount = int( solid * 0.01 )
            less += mount*2
            if isout(y+1, x+1): out += mount
            else: maps[y+1][x+1] += mount 
            if isout(y+1, x-1): out += mount
            else: maps[y+1][x-1] += mount 

            mount = int( solid * 0.05 )
            less += mount
            if isout(y-2, x): out += mount
            else: maps[y-2][x] += mount 

            if isout(y-1, x): out += solid - less
            else: maps[y-1][x] += solid - less 

            
        if dir == 2:
            mount = int( solid * 0.01 )
            less += mount*2
            if isout(y-1, x-1): out += mount
            else: maps[y-1][x-1] += mount 
            if isout(y-1, x+1): out += mount
            else: maps[y-1][x+1] += mount 

            mount = int( solid * 0.1 )
            less += mount*2
            if isout(y+1, x+1): out += mount
            else: maps[y+1][x+1] += mount 
            if isout(y+1, x-1): out += mount
            else: maps[y+1][x-1] += mount 

            mount = int( solid * 0.05 )
            less += mount
            if isout(y+2, x): out += mount
            else: maps[y+2][x] += mount 

            if isout(y+1, x): out += solid - less
            else: maps[y+1][x] += solid - less 

    elif dir in [3, 4]:
        mount = int( solid * 0.07 )
        less += mount*2
        if isout(y-1, x): out += mount
        else: maps[y-1][x] += mount 
        if isout(y+1, x): out+= mount
        else: maps[y+1][x] += mount 

        mount = int( solid * 0.02 )
        less += mount*2
        if isout(y-2, x): out += mount
        else: maps[y-2][x] += mount 
        if isout(y+2, x): out += mount
        else: maps[y+2][x] += mount 

        if dir == 3:
            mount = int( solid * 0.1 )
            less += mount*2
            if isout(y-1, x-1): out += mount
            else: maps[y-1][x-1] += mount 
            if isout(y+1, x-1): out += mount
            else: maps[y+1][x-1] += mount 

            mount = int( solid * 0.01 )
            less += mount*2
            if isout(y+1, x+1): out += mount
            else: maps[y+1][x+1] += mount 
            if isout(y-1, x+1): out += mount
            else: maps[y-1][x+1] += mount 

            mount = int( solid * 0.05 )
            less += mount
            if isout(y, x-2): out += mount
            else: maps[y][x-2] += mount 

            if isout(y, x-1): out += solid - less
            else: maps[y][x-1] += solid - less 


        elif dir == 4:
            mount = int( solid * 0.01 )
            less += mount*2
            if isout(y-1, x-1): out += mount
            else: maps[y-1][x-1] += mount 
            if isout(y+1, x-1): out += mount
            else: maps[y+1][x-1] += mount 

            mount = int( solid * 0.1 )
            less += mount*2
            if isout(y+1, x+1): out += mount
            else: maps[y+1][x+1] += mount 
            if isout(y-1, x+1): out += mount
            else: maps[y-1][x+1] += mount 

            mount = int( solid * 0.05 )
            less += mount
            if isout(y, x+2): out += mount
            else: maps[y][x+2] += mount 

            if isout(y, x+1): out += solid - less
            else: maps[y][x+1] += solid - less 

    
    return maps, out

dir = 3
size = 1
y, x = n//2, n//2
result = 0
t_map = [ [ 0 for i in x ] for x in maps]
while True:
    t_map[y][x] = 1
    if dir == 1:
        maps, out = tornaido(y-1, x, dir, maps)
        
        y, x = y - size, x
        if t_map[y][x-1] == 0: dir = 3
    elif dir ==2:
        maps, out = tornaido(y+1, x, dir, maps)
        
        y, x = y + size, x
        if t_map[y][x+1] == 0: dir = 4
    elif dir == 3:
        maps, out = tornaido(y, x-1, dir, maps)
        y, x = y, x - size
        if t_map[y+1][x] == 0: dir = 2
    else:
        maps, out = tornaido(y, x+1, dir, maps)
        y, x = y, x + size
        if t_map[y-1][x] == 0: dir = 1

    result += out
    if y==0 and x == 0:
        break
    
print(result)
