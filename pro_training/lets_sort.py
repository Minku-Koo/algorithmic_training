# lets_sort
#  "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

def solution(size, arr):
    convert_num = {
         "ZRO":0, "ONE":1, "TWO":2, "THR":3, 
         "FOR":4, "FIV":5, "SIX":6, "SVN":7, 
         "EGT":8, "NIN":9
    }
    convert_str = { v:k for k, v in convert_num.items()}
    
    numbers = []
    for n in arr:  
        if convert_num.get(n)==None: print(n)
        numbers.append( convert_num.get(n) )
    snum = sorted(numbers)
    return " ".join( [ convert_str.get(x) for x in snum ] )

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    _, size = list(map(int, input().split()  ))
    arr = list(input().split() )
    print("--")
    print(f"#{test_case} {solution(size, arr)}")

#1

#ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO...
#2

#ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO... 