#m2string

def solution(search, base):
    result = 0
    size, bsize = len(search), len(base)
    for i, ch in enumerate(base):
        if i==bsize-size +1: break
        if base[i:i+size]==search: result+=1
    return result

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    _ = input()
    search = input()
    base = input()
    print(f"#{test_case} {solution(search, base)}")

#1 4
#2 2
#3 19
#4 4
#5 6
#6 2
#7 5
#8 5
#9 8
#10 14