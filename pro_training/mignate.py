# 1은 N극 성질을 가지는 자성체를 2는 S극 성질을 가지는 자성체
# 윗부분에 N극이 아래부분에 S극

def solution(size, box):
    result = 0
    
    def check(stack):
        check_ = 0
        while stack:
            el = stack.pop()
            if el==1: continue
            if stack and el == 2 and stack[-1] == 1:
                check_ += 1
            
        return check_
    
    # 세로로 뽑아서 스택에 넣고, 하나씩 뽑으면서 카운트
    for x in range(size):
        line = []
        for y in range(size):
            el = box[y][x]
            if el!=0: line.append(el)
        result += check(line)
            
    return result


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    side = int(input())
    box = []
    for j in range(side):
        box.append( list(map( int, input().split() )) )
        
    print("#"+str(test_case), end=' ')
    print( solution( side, box ) )



#1 471
#2 446
#3 469
#4 481
#5 481
#6 501
#7 488
#8 476
#9 464
#10 490
