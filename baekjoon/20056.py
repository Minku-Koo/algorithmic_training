"""
Date : 21.10.23
Problems : https://www.acmicpc.net/problem/20056
Title : 마법사 상어와 파이어볼
"""
# BFS

def solution( n, m, k, fire ):
    
    def move(file):
        # print(file)
        for id, b in enumerate(file):
            # print("b",b)
            y, x = tuple(b[:2])
            fast, dir = b[3:]
            dy, dx = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]
            for j in range(fast):
                ny, nx = y+dy[dir], x+dx[dir]
                if ny<0: ny = n+ny
                elif ny>=n : ny = ny-n

                if nx<0: nx=n+nx
                elif ny>=n: nx-=n
                y, x = ny, nx
            file[id][0]=y
            file[id][1]=x
        return file

    # 합쳐진거 나누기
    def sep(file):
        ln = len(file)
        visit= []
        for id in range(ln):
            same = []
            for jd, bl in enumerate(file):
                if jd==id : continue
                if file[id][:2]==bl[:2]:
                    # 같은위치
                    same.append( bl )
            if not same: continue
            if tuple(bl[:2]) in visit: continue
            same.append( file[id] )
            # print(same)
            w = 0
            od =[]
            fst =0
            y, x = same[0][:2]
            visit.append((y,x))
            for b in same:
                file.remove(b)
                w+=b[2]
                fst += b[3]
                od.append(b[-1])
            
            dirs = []
            for s in od:
                if s%2==0: dirs.append(1)
                else: dirs.append(0)
            dir_ = True if len(set(dirs))==1 else False
            dirr = [0,2,4,6] if dir_ else [1,3,5,7]
            # file[id] = [ y, x, file[id][2]+w, 
            #     (file[id][3]+fst)//(len(same)+1) , dirr[0] ]
            for d in dirr:
                file.append( [ y, x, w//5, 
                fst//(len(same)+1) , d ] )
        return file
                    


    for _ in range(k):
        # 이동하기
        fire = move(fire)
        # for j in fire: print('>',j)
        # print("**"*10)
        # 합친거 나누기
        fire = sep(fire)
        # for j in fire: print('>',j)

    result = sum( [w[2] for w in file])

    return result


if __name__ == "__main__":
    n, m, k =list(map(int, input().split()))
    file = []
    for i in range(m):
        file.append(list(map(int, input().split())))
    
    print(solution(n, m, k, file)  )

