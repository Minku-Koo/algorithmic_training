
def solution(w, h, box):
    width = 56
    real_code = []
    for code_line in box:
        if sum(code_line)==0: continue
        else: break
    
    for num in code_line[::-1]:
        if num==1:
            real_code += num
        if len(real_code)==56: break
    code = [x for x in reverse(real_code)[::4]]
    print(code)
    return 

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    w, h = list(map(int, input().split()))
    box = [i for i in input()]
    print("#"+str(test_case), end=" ")
    print(solution(w, h, box))
