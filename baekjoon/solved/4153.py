"""
Date : 21.03.24
URL : https://www.acmicpc.net/problem/4153

[Problems]
과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 
주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

[Input]
입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다. 
각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.

[Output]
각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.

"""
def solution():
    input_ = input().split(" ") # 공백으로 분리
    a, b, c = int(input_[0]), int(input_[1]), int(input_[2])
    if a==0 and b==0 and c==0: return False # 모두 0이면 종료

    numbers = [a, b, c] # 입력값 리스트 생성
    long_side= max(numbers) # 제일 긴 변 길이
    numbers.remove(long_side) # 제일 긴 변 제거
    
    # 가장 긴 변 보다 나머지 두 변의 길이 합이 작으면
    if numbers[0] + numbers[1] <= long_side : 
        print("wrong")
        return True
    
    # 직각 삼각형 조건 만족할 경우
    if long_side **2 == (numbers[0]**2 + numbers[1]**2) :print("right")
    else: print("wrong")
        
    return True

if __name__ == "__main__":
    # False 반환까지 반복
    while solution(): pass
    