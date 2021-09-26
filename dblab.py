'''
/***
- 파이썬 언어를 사용해서 풀어주세요
- 문제는 다 푸는대로 카톡으로 전체 코드를 보내주세요
- 파이썬 기본 내장함수만 활용 가능합니다. (import 불가능)
- 체점 요소 : 정확성, 효율성, 가독성
****/

대소문자가 구별되지 않는 알파벳 문자열 변수 abc가 존재한다.
알파벳은 중복되어 등장할 수 있는데, 이때 알파벳 사이의 거리가 가장 긴 알파벳을 구하라.
단, 결과는 대문자로 통일한다.

'알파벳 사이의 거리'는 동일한 알파벳 사이에 모두 다른 알파벳이 들어가있는 경우이다.
예를 들면, AAaA에서 A의 거리는 0이다. aayaay에서 A의 거리는 1, Y의 거리는 2이다.

# 중복된 알파벳이 없다면, ERR을 반환하라
# 알파벳 사이 거리가 동일한 알파벳이 2개 이상 나타난다면, 가장 빠른 알파벳(A가 빠르고 Z가 느림)을 반환하라

예시 1)
abc = "DnhowkhOdmS"
>> D

예시 2)
abc = "DBkjUpECa"
>> ERR

예시 3)
abc = "txLbexoBEezq"
>> B

예시 4)
abc = "aaaaaaaaa"
>> A

/** 답안 작성 예시
def solution(abc):
    # write your code
    return answer
**/
'''


def solution(abc):
    max_leng = 0
    max_alpha = "ERR"
    
    for i in range(len(abc)):
        leng = 0
        
        for j in range(i+1, len(abc)):
            if abc[i].lower() == abc[j].lower():
                if leng >= max_leng:
                    max_leng = leng
                    temp = max_alpha
                    max_alpha = abc[i]
                    
                if (leng == max_leng)  and temp!="ERR" and ord(abc[i]) > ord(temp):
                    max_alpha = temp
                    
                break
                
            else:
                leng += 1
       
    return max_alpha.upper()
    



if __name__ == "__main__":
    abc_list = [
        "DnhowkhOdmS", # D
        "DBkjUwOpECa",  # ERR
        "tbLweboWEezq", # B
        "yyyyyyyyaaaaa", # A
        "halaalallalh", # H
        "yuihjkBNMEDR", # ERR
        "AAAAaaaAAAAAaaAa", # A
        "YuuuYuuuyzzzIzzzzzizzY", # Y
        ]

    for abc in abc_list:
        print(f"{abc} >> {solution(abc)}")