"""
Date : 21.10.20
Problems : https://www.acmicpc.net/problem/14888
Title : 연산자 끼워넣기
"""
# BFS

def solution(n, nums, ops):
    
    # 1:"+",
    # 2:"-",
    # 3:"*",
    # 4:"/"

    def calc(nums, ops):
        result = nums[0]
        for i in range(len(ops)):
            if ops[i]==3: result *= nums[i+1]
            elif ops[i]==2: result -= nums[i+1]
            elif ops[i]==4: 
                if result<0: result = ((result* -1) // nums[i+1]) * -1
                elif result==0: result = 0
                else: result = result // nums[i+1]
            else: result += nums[i+1]
            
        return result


    op_combine = []
    comb = []
    def getCombine_dfs(line, n):
        if len(comb)==n-1:
            
            op_combine.append(comb[:])
            return
        
        setline = set([l for l in line])
        for p in setline:
            comb.append(p)
            ind = line.index(p)
            newline = line[:]
            
            del newline[ind]
            
            getCombine_dfs(newline, n)
            comb.pop()

        return
    start = []
    for j in range(len(ops)):
        for i in range(ops[j]):
            start.append(j+1)
            
    getCombine_dfs(start, n)
    

    maxv, minv = -99*99, 99*99
    for line in op_combine:
        result = calc(nums, line)
        if result>maxv: maxv=result
        if result<minv: minv=result

    return maxv, minv


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    ops = list(map(int, input().split()))

    m1, m2 = solution(n, nums, ops)
    print( m1, m2  )



