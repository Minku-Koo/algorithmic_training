#pelindrom

def check(arr):
    if arr == arr[::-1]: return True
    return False

def solution(size, box):
    result = 0
    BOX_SIZE = 8
    for line in box: # 가로부터 판별
        for i in range(BOX_SIZE-size+1):
            if check(  line[i:i+size] ):
                result +=1
                
    for x in range(BOX_SIZE): # 세로
        subline = []
        for y in range(BOX_SIZE):
            subline.append( box[y][x] )
        for i in range(BOX_SIZE-size+1):
            if check(  subline[i:i+size] ):
                result +=1
    return result

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    size = int(input())
    box = []
    for _ in range(8):
        box.append( list(input()) )
    print(f"#{test_case} {solution(size, box)}")

#1

#ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO...
#2

#ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO... 