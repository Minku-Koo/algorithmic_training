"""
Date : 21.10.07
Problems : https://www.acmicpc.net/problem/17825
Title : 주사위 윷놀이 
"""

# 

# 말 위치 초기화
loc = [[0,0],[0,0],[0,0],[0,0]]
# 윷놀이 판
maps = {
    0: [],
    10: [13,16,19,25,30,35,40, 100],
    20: [22,24,25,30,35,40, 100],
    30: [28,27,26,25,30,35,40, 100],
}

def setting():
    maps[0] = [j*2 for j in range(21)] + [100]

result = []

def dfs(map, node, play, count, visit=[]):
    # print("-----", count)
    if count==10: 
        result.append(visit[:])
        return 
    # print("count/node",count, node)
    # print("visit", visit)
    # if node not in visit:
    # 말 4개에 대해 다음 칸으로 이동
    move = play[count]

    nnode = [list(s) for s in node]
    loop_list = []
    for i, n in enumerate(node):
        start, num = n
        if num in [10, 20, 30]:
            ky = num
            idx, num = move-1, map[num][move-1]
        elif start in  [10, 20, 30]:
            ky = start
            idx, num = move-1, map[start][move-1]
        else:
            idx = map[start].index(num)
            num = map[start][idx+move]
            ky = 0

        # 말이 겹칠 경우
        if [ky, num] in node and num != 100: continue
        else:
            nnode[i] = [ky, num]

        n_loc = tuple([tuple(j) for j in nnode])
        loop_list.append(n_loc)
        nnode[i] = n
    
    for lp in set(loop_list):
        visit.append( lp )
        dfs(map, lp, play, count+1, visit )
        visit.pop()

    return 



def solution(play, loc):
    print("loc", tuple([tuple(k) for k in loc]) )
    dfs(maps, tuple([tuple(k) for k in loc]), play, 0)
    print( len(result) )

    print(result[0])

    maxv = 0
    for r in result:
        sm = [[],[],[],[]]
        for el in r:
            sm[0].append(el[0][1])
            sm[1].append(el[1][1])
            sm[2].append(el[2][1])
            sm[3].append(el[3][1])
        ss = [sum(list(set(j))) for j in sm]
        if maxv < sum(ss):
            maxv = sum(ss)
    print(">>", maxv)
    return 




if __name__ == "__main__":
    play = list(map(int, input().split()))
    print(play)
    
    setting()

    solution(play, loc)

    pass
