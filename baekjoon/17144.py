"""
Date : 21.03.24
URL : https://www.acmicpc.net/problem/17144
"""

def solution(number, line):
    new_line = []
    max_calc = number // 2
    max_calc = max_calc // 2 if max_calc % 2 == 0 else max_calc //2 + 1


    
    for index, num in enumerate(line):
        pass
            
    print(new_line)

    return True

if __name__ == "__main__":
    number =1# int(input())
    line =  "3+8*7-9*2" #input()
    solution(number, line)
    