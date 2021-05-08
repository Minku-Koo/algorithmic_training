# 21.05.08


def solution(s):
    answer = ''
    nums = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    temp = ""
    for c in s:
        if c.isdigit(): # 숫자일 경우
            answer += str(c)
            temp = ""
        else:
            temp += c
            if temp in nums.keys():
                answer += str(nums[temp])
                temp = ""
                
    return int(answer)
    