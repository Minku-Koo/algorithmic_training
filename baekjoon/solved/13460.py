"""
Date : 21.10.17
Problems : https://www.acmicpc.net/problem/13460
Title : 구슬 탈출2
"""

def solution(height, width, box):
    for y in range(height):
        for x in range(width):
            if box[y][x]=="R": red = [y,x]
            elif box[y][x]=="B": blue = [y,x]
            
    # bfs
    def move(y, x, dir):
        if dir=="u": ny, nx = -1, 0
        elif dir=="d": ny, nx = 1, 0
        elif dir=="r": ny, nx = 0, 1
        elif dir=="l": ny, nx = 0, -1 

        while True:
            next = box[y+ny][x+nx]
            if next == "O": return "out", -1, -1
            if next == "#": break
            else: y, x = y+ny, x+nx
        return "go", y, x

    def bfs(red, blue):
        count = 0
        q = [(red, blue, "", count)]
        other_side = {
            "d":"u", "u":"d", "l":"r", "r":"l"
        }
        while q:
            red, blue, org_dir, count = q.pop(0)
            
            if count>10: return -1
            ry, rx = red
            by, bx = blue
            
            for d in ['r','l','u','d']:
                 #왔던 길 제외
                if org_dir and d==other_side[org_dir] : continue

                # 상 하 좌 우 이동
                rresult, nry, nrx = move(ry, rx, d)
                bresult, nby, nbx = move(by, bx, d)
                
                # if 이동시 out에 걸리는지 확인
                if bresult == "out": continue
                # red는 나가고 blue는 남는 경우 > 성공
                elif rresult=="out" and bresult=="go": return count+1
                # r과 b 같으면 늦은 쪽 보정해서 1 뒤로
                elif (nry , nrx) == (nby , nbx):
                    if d=="u":
                        if ry < by: nby += 1
                        else: nry += 1
                    elif d=="d":
                        if ry > by: nby -= 1
                        else: nry -= 1
                    elif d=="r":
                        if rx < bx: nrx -= 1
                        else: nbx -= 1
                    elif d=="l":   
                        if rx > bx: nrx += 1
                        else: nbx += 1
                    
                # 안걸리면 q 추가
                if (ry, rx)==(nry,nrx) and (by, bx)==(nby,nbx): continue
                q.append( ((nry, nrx), (nby, nbx), d, count+1)  )

        return -1
    
    result = bfs(red, blue)
    return -1 if result>10 else result


if __name__ == "__main__":
    height,width =list(map(int, input().split()))
    box = []
    for i in range(height):
        box.append( [j for j in input()] )

    print(solution(height, width, box))

