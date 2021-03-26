"""
Date : 21.03.25
Problems : https://www.acmicpc.net/problem/16637
"""

def solution(number, line):
    def calculation(lines): # 연산 함수
        # input : 계산식 (string)
        # output : 결과값 (int)
        
        if lines[0] == "-":   # 계산식 처음이 음수라면
            lines = "0"+lines # 맨 앞에 0 추가
        
        nums = "" # 두자리 이상 숫자 계산 위해
        line = [] # 계산할 식 담을 리스트 선언
        for i in lines:
            if i.isdigit() == False: #문자일 때
                if nums != "": # 숫자가 담긴 경우
                    line.append( nums ) #리스트에 숫자 추가
                line.append( i ) #리스트에 연산자 추가
                nums = "" #숫자 초기화
            else:
                nums += i #연산자 추가
        line.append(nums) #마지막 숫자 추가
        

        result = int(line[0]) # 계산값 처음에 첫번째 숫자 선언
        for index, c in enumerate(line[1:]):
            if c.isdigit(): # 숫자일 경우
                op = line[index] 
                if op == "+": result += int(c) #덧셈 계산
                elif op == "-":  # 뺄셈 계산
                    if line[index-1] == "*": # 만약 곱셈과 연속일 경우
                        result *= int(c) * -1 # 음수로 곱셈 연산
                    else:
                        result -= int(c) # 뺄셈 연산
                    
                else : result *= int(c) # 곰셈 연산
        
        return result
    
    def newLine_fromIndex(index, line):
        # 연산자 인덱스를 입력하면 계산해서 새로운 계산식 반환
        
        a, b, result = int(line[index-1]), int(line[index+1]), 0
        
        # 연산자 따라서 계산
        if line[index] == "+": result = a + b
        elif line[index] == "-": result = a - b
        else : result  = a * b

        if result < 0: # 계산값이 음수일 경우
            if line[index-2] == "+": # 이전 연산자가 덧셈일 때 -> 덧셈 제거
                new_line = line[:index-2] + str(result) + line[index+2:]
            elif line[index-2] == "-": # 이전 연산자가 뺄셈일 때 -> 덧셈으로 변환
                new_line = line[:index-2] + "+" + str(result*-1) + line[index+2:]
            else: # 이전 연산자가 곱셈일 때 -> 그대로
                new_line = line[:index-1] + str(result) + line[index+2:]
        else:
            new_line = line[:index-1] + str(result) + line[index+2:]

        # 결과 계산식 맨 앞이 음수일 경우 -> 맨 앞에 0 붙여줌
        if new_line[0] == "-" : new_line = "0"+new_line
        return new_line

    def permute(array, r): # 중복 제거 조합 계산
        for i in range(len(array)):
            if r == 1: # 종료 조건
                yield [array[i]]
            else:
                for next in permute(array[i+1:], r-1):
                    yield [array[i]] + next

    def calc_position(count, length): 
        # count : 몇 개의 괄호를 칠 지 받고
        # length : 총 연산식 길이
        # 중복 없이 괄호 위치를 반환
        result = []
        # 연산자 위치 인덱스 리스트
        calc_list = [ x for x in range(length)  if x%2 ==1 ]
        # 중복 제거한 조합 계산
        _list = [ x for x in permute(calc_list, count) ]

        for nums in _list:
            isTrue = True
            for num in nums: # 조합이 연속으로 존재하는 경우 -> 제거
                if num-2 in nums or num+2 in nums: 
                    isTrue = False
                    break
            # 연속으로 존재하지 않으면 -> 결과 조합에 추가
            if isTrue: result.append( nums )

        return result
                
        
    max_output = -1 * (2 ** 31) # 최대 결과값 저장 변수 (최소값으로 초기화)

    max_calc = number // 2
    # 괄호 최대 개수
    max_bracket = max_calc // 2 if max_calc % 2 == 0 else max_calc //2 + 1

    num = 1 # 괄호 개수
    while num < max_bracket+1 : #괄호 개수를 최대값까지 반복
        for position in calc_position(num, number): # 조합 개수 전달
            # 새로운 계산식 복사
            newline = "".join([ x for x in line ])
            for p in sorted(position, reverse=True):
                # 연산자 괄호친 것 우선 계산 -> 새로운 계산식 반환
                newline = newLine_fromIndex(p, newline)

            value = calculation( newline) # 결과 계산
            # 계산식 초기화
            newline =  "".join([ x for x in line ])
            if max_output < value: # 최대값보다 결과값이 크면
                max_output = value #최대값 = 결과값
    
        num += 1
    value = calculation( line) # 괄호 아무것도 치지 않고 계산한 경우
    if max_output < value:
        max_output = value

    return max_output


if __name__ == "__main__":
    number = int(input())
    line =   input()
    
    print( solution(number, line) )
    