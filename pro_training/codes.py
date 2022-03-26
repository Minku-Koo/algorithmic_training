
def solution(w, h, box):
    ndict = {
        '0001101':0,
        '0011001':1,
        '0010011':2,
        '0111101':3,
        '0100011':4,
        '0110001':5,
        '0101111':6,
        '0111011':7,
        '0110111':8,
        '0001011':9,
    }
    width = 56
    real_code = ""
    for code_line in box:
        if set([j for j in code_line])=={'0'}: continue
        else: break
    
    plz_input = False
    for num in code_line[::-1]:
        if num=='1': plz_input = True
        if plz_input: real_code += num
        if len(real_code)==width: break
    real_code = list(real_code)[::-1]
    code = [ndict[''.join(real_code[i*7 : i*7+7])] for i in range(8)]
    
    numsum = (code[0]+code[2]+code[4]+code[6])*3+(code[1]+code[3]+code[5])+code[-1]
    result = 0 if numsum % 10!=0 else sum(code)
    return result

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    h, w = list(map(int, input().split()))
    box = [input() for i in range(h)]
    print("#"+str(test_case), end=" ")
    print(solution(w, h, box))
