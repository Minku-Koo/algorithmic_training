"""
Date : 21.04.20
Problems : https://www.acmicpc.net/problem/13458
Title : 시험 감독 
"""

class TestChecker:
    def __init__(self, N, student, B, C):
        self.N = N
        self.student = student
        self.B, self.C = B, C

    # n명이 있는 교실에 필요한 최소 감독관 구하기
    def howManyChecker(self, n):
        n -= self.B # 총감독관 관리 인원 제외
        checker = 1 # 총감독관 추가
        if n < 0: n = 0 # 음수일 경우 -> 0으로 재설정
        if n % self.C == 0: # 나누어 떨어질 경우
            checker += n // self.C 
        else: # 나머지가 있는 경우
            checker += n // self.C + 1
        return checker

    def getResult(self): # 결과값 구하기
        result = 0
        for a in self.student: # 모든 시험장 인원
            # 시험장당 필요한 감독관 수 계산
            result += self.howManyChecker(a) 
        return result


if __name__ == "__main__":
    N = int(input())
    student = list(map(int, input().split()))
    B, C = map(int, input().split())
    
    test_checker = TestChecker(N, student, B, C)
    result = test_checker.getResult()
    print(result)

    