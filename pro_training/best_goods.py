
def solution(a, b):
    time_set = 18
    not_primes = [0,1,4,6,8,9,10,12,14,15,16,18]
    def calc(p): # 장인이 p 확률로 완제품 만들 때
        percent = 0.0
        p *= 0.01
        for num in not_primes:
            base, child = 1, 1
            for x in range(1, num+1): base *= x
            for y in range(time_set + 1 - num , time_set+1): child *= y
            percent += ((p ** num) * ((1-p)**(time_set-num))) * (child/base)#확률  NCn
        return percent # 소수 아닌 완제품 확률
    
    result = ( calc(a) * calc(b) ) # 둘 다 소수 아닌 완제품 만든 확률
    return 1 - round(result, 6)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b = list(map(int, input().split()))
    print("#"+str(test_case), end=" ")
    print("%0.6f" %solution(a, b ))
    
    