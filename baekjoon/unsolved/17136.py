"""
Date : 21.04.18
Problems : https://www.acmicpc.net/problem/17136
Title : 색종이 붙이기
"""

# 아직 못품

def solution(map):

    def checkBoxCoords(size):
        coords = []
        num = (size - 1) * -1 if size != 1 else len(map)
        for y, line in enumerate(map[:num]):
            for x, cell in enumerate(line[:num]):
                if cell == "0": continue
                
                isBox = True
                for j in range(size):
                    if not isBox: break
                    for i in range(size):
                        if map[y+j][x+i] != "1" :
                            isBox = False
                            break
                
                if isBox: coords.append( (y, x) )
        return coords
    
    def removeRegions(y, x, size, map):
        for j in range(size):
            for i in range(size): map[y+j][x+i] = "0"
        return map

    def permute(boxList):
        result = []
        lenBox = len(boxList)
        permutation = []
        
        def dfs(boxs):
            if len(permutation) == lenBox:
                result.append(permutation[:])
                return
            if len(result) >1000:
                #result.append(permutation[:])
                #permutation = []
                return

            for w in boxs:
                permutation.append(w)
                newBox = boxs[:]
                newBox.remove(w)
                dfs(newBox)
                permutation.pop()
        
            return
        dfs(boxList[:])
        return result
            
    
    def calc(map):
        path = {1:0, 2:0, 3:0, 4:0, 5:0}
        result = []
        def dfs(map, path, size = 5):
            
            if size == 1:
                oneCount = sum([x.count("1") for x in map])
                if oneCount > 5: path[1] = -1
                else : path[1] = oneCount
                
                result.append(path)
                return


            boxCoods = checkBoxCoords(size)
            lists = permute(boxCoods)

            for w in lists:
                for y, x in w: 
                    if map[y][x] == "1":
                        map = removeRegions(y, x, size, map[:])
                        path[size] += 1

                dfs(map[:], path, size -1)
            return

        dfs(map[:], path)
        
        return result
    
    result = calc(map[:])
    maxVal = 5 * 5 + 1
    val = maxVal
    
    for r in result:
        if r[1] == -1: continue
        if r[2] >5 or r[3] >5 or r[4] > 5: continue
        if sum([r[x] for x in r]) < val: 
            val = sum([r[x] for x in r])

    if val  == maxVal : val =  -1

    return val



if __name__ == "__main__":
    map = []
    for _ in range(10):
        #map.append( input().replace("\n", "").split() )
        pass
    #print( solution(map) )




    a = """
1 1 1 1 0 1 1 1 1 1
1 1 1 1 0 0 1 1 1 1
1 1 1 1 0 0 1 1 1 1
1 1 1 1 0 0 1 1 1 1
1 1 1 1 0 0 1 1 1 1
1 1 1 1 0 0 1 1 1 1
1 1 1 1 0 0 1 1 1 1
1 1 1 1 0 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
"""
    aa = """
0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 0 1 0 0 1 1 1 1 1
0 0 0 0 0 1 1 1 1 1
0 0 0 0 0 1 1 1 1 1
0 0 0 0 0 0 0 1 1 1
0 0 1 0 0 0 0 1 1 1
0 0 0 0 0 0 0 1 1 1
0 0 0 0 0 0 1 1 1 1
0 0 0 0 0 0 1 1 1 1
"""
    list_ = a.strip("\n").split("\n")
    for i in list_:
        map.append( i.split() )

    print("result>>", solution(map) )
    
   