# 21.04.14
# p.331
# Problem Title : 섬의 개수

def solution(map):
    map = map.strip("\n").split("\n")
    map = [ [ i for i in x ] for x in map ]
    
    def dfs(j, i, maps):
        if j<0 or j >= len(maps) or \
        i<0 or i >= len(maps[0]) or \
        maps[j][i] == "0":
            return maps

        maps[j][i] = "0"
        maps = dfs(j, i+1, maps)
        maps = dfs(j, i-1, maps)
        maps = dfs(j+1, i, maps)
        maps = dfs(j-1, i, maps)

        return maps

    count = 0
    for j in range(len(map)):
        for i in range(len(map[0])):
            if map[j][i] == "1":
                map = dfs(j, i, map)
                count += 1
    
    return count

if __name__ == "__main__":
    maps = """
000110000
000101110
110000010
100110000
"""
    
    result = solution(maps)
    print(result)
