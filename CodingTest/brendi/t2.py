#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, lowerBound, upperBound):
        checked = [0, 1] #제곱수 초기화 
        result = [] #결과값 초기화
        for n in range(2, upperBound+1): # 2이상 숫자 제곱수 계산
            a = 2
            while True:
                cal = n ** a #거듭제곱수
                if cal > upperBound: break #최댓값보다 커지면 종료
                checked.append(cal)
                if lowerBound <=cal: #범위 사이일 경우
                    result.append(cal)
                a+=1

        checked = sorted(checked)
        step = False
        # 거듭제곱수 끼리 더해서 완전거듭제곱수합 계산
        for a, i in enumerate(checked):
            for b, j in enumerate(checked[a:]):
                if b ==0 and i+j > upperBound: 
                    step = True
                    break
                if lowerBound <=i+j <= upperBound:
                    result.append(i+j)

            if  step: break
        
        return len(list(set(result)))
    

if __name__ == "__main__":
    
    s = Solution()
    ans = s.solution(1, 5000000)
    #ans = s.solution(25, 31)
    # 33604
    print(ans)