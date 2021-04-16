# 21.04.14
# p.338
# Problem Title : 전화 번호 문자 조합

def solution(number):
    phone = {
        2 : "abc",
        3 : "def",
        4 : "ghi",
        5 : "jkl",
        6 : "mno",
        7 : "pqrs",
        8 : "tuv",
        9 : "wxyz"
    }

    def dfs(path, index):
        if len(path) == len(number):
            result.append(path)
            return
        
        for i in range(index, len(number)):
            for d in phone[ int(number[i]) ]:
                dfs(path+d, i+1)

    result = []
    dfs("", 0)

    return result

if __name__ == "__main__":
    number = "256"
    result = solution(number)
    print(result)
