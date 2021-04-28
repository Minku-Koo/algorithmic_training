"""
Date : 21.04.24
Problems : https://www.acmicpc.net/problem/20058
Title : 마법사 상어와 파이어스톰
"""

class WizardFirestorm:
    def __init__(self, n, q, place):
        self.n, self.q = n, q
        self.place = place

    # 파이어스톰 위치 계산
    def calcFireballLoc(self, num, place):
        newPlace = [ a[:] for a in place]
        size = 2 ** num # 파이어볼 크기
        placeSize = 2 ** self.n # 전체 크기
        for y in range(0, placeSize, size ):
            for x in range(0, placeSize, size ):
                # 해당 파이어스톰 영역 회전
                newPlace = self.rotation(y, x, num, newPlace)
        return newPlace

    # 해당 영역 회전
    def rotation(self, y, x, size, place):
        # 전체 지도
        newPlace = [ a[:] for a in place]
        # 파이어스톰 영역
        box = [[0 for _ in range(2**size) ] for _ in range(2**size)]

        for line in newPlace[y:y+2**size]:
            for index, ice in enumerate( line[x:x+2**size] ):
                # 90도 회전
                box[index].insert(0, ice)

        for y_ in range(2**size):
            for x_ in range(2**size):
                # 90도 회전된 영역 재입력
                newPlace[y+y_][x+x_] = box[y_][x_]

        return newPlace

    # 얼음 제거
    def removeIce(self, place):
        newPlace = [a[:] for a in place]
        icePlace = [a[:] for a in place]
        plus = [[1,-1,0,0],[0,0,1,-1]]
        
        # 전체 칸 계산
        for y in range(len(place)):
            for x in range(len(place)):
                noice, ice = 0, 0
                for d in range(4): # 상하좌우 계산
                    y_, x_ = y + plus[0][d], x + plus[1][d]
                    # 영역 밖으로 벗어난 경우
                    if y_<0 or x_<0 or y_> len(place) -1 or x_> len(place) -1:
                        noice += 1
                        continue
                    elif newPlace[y_][x_] <= 0 : 
                        noice +=1
                    else: 
                        ice +=1
                        if ice >= 3:
                            break
                        
                if noice >=2: # 얼음 인접하지 않은게 2개 이상이면
                    # 얼음 1 제거
                    if newPlace[y][x]>=1: icePlace[y][x] -= 1

        return icePlace

    # 총 합 구하기
    def sumIce(self, place):
        result = 0
        for line in place:
            result += sum(line)
        return result

def bigSize(place):
    newPlace = [a[:] for a in place]
    plus = [[1, -1, 0, 0], [0, 0, 1, -1]]
    result = []
    maxSize = 0
    keeps = False
    length = len(place)

    for y in range(length):
        if keeps: break
        if sum(newPlace[y]) <1: continue
        for x in range(length):
            if newPlace[y][x] >0:
                newPlace[y][x] = 0
                queue = [(y, x)]
                check = []
                while queue:
                    iy, ix = queue.pop(0)
                    check.append( (iy, ix) )
                    
                    for d in range(4):
                        y_, x_ = iy + plus[0][d], ix + plus[1][d]
                        if (y_, x_) in check : pass
                        elif y_ < 0 or x_ < 0 or y_ > length - 1 or x_ > length - 1:
                            pass
                        elif newPlace[y_][x_]==0: pass
                        else:
                            queue.append( (y_, x_) )
                            newPlace[y_][x_] = 0


                size = len(  list(set(check))  )
                result.append( size )
                if size > maxSize:
                    maxSize = size
                    
                if sum(result) == length**2: 
                    keeps = True
                    break

    return maxSize



if __name__ == "__main__":
    n, q = map(int, input().split())
    place = []
    for _ in range(2**n): place.append(list(map(int, input().split())))
    order = list(map(int, input().split()))

    wizard = WizardFirestorm(n, q, place)
    
    for size in order:
        # 파이어스톰 위치 계산
        place = wizard.calcFireballLoc(size, place)
        # 얼음 제거
        place = wizard.removeIce(place)
    # 총 합 구하기
    sums = wizard.sumIce(place)
    print( sums)
    # 최대 얼음 사이즈 구하기
    big = bigSize(place)
    print(big)
