
def solution(N):
    def check(n): # 정답 확인 함수
        n = n[::-1] # 1의 자리부터 오름차순으로 확인
        # 인덱스를 확인
        for index, j in enumerate(n[:-1]):
            # 같은 문자 연속이면, 인덱스 반환 (=자리수)
            if j == n[index+1]: return index
        return -1 #정답인 경우

    N += 1
    while True: #정답일때까지 반복
        result = check(str(N))
        # 정답인 경우
        if result == -1: return N
        # 자릿수만큼 더해줌
        N += 10**result
        # 더해준 자릿수 이하 0으로 초기화
        N = int(str(N)[:len(str(N))-result] + "0"*result)