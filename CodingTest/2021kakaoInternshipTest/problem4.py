#21.05.08

def solution(n, start, end, roads, traps):
    answer = 0
    
    def canGo(road, now):
        results = []
        for r in road:
            if r[0] == now :
                results.append( r[1:] )
        return results
    
    def ohTrap(road, t):
        newroad = []
        for r in road:
            if r[0] == t or r[1] == t:
                newroad.append([ r[1], r[0], r[2] ])
            else:
                newroad.append(r)
        return newroad
    
    result = []
    check = []
    dists = []
    smallest = [99999]
    ends = [end]
    
    def dfs(node, road):
        if sum(dists[:]) >= smallest[0]:
            return
        if node == ends[0]:
            sumd = sum(dists[:])
            result.append(sumd)
            if sumd < smallest[0]:
                smallest[0] = sumd
            return
        if check.count(node)>3:
            return
        
        elif node in traps:
            road = ohTrap(road, node)

        cango = canGo(road, node)
        if cango == []: return
        
        for w in sorted(cango, key=lambda x:x[1]):
            target, dist = w
            check.append(target)
            dists.append(dist)
            
            dfs(target, [ r[:] for r in road])
            
            check.pop()
            dists.pop()
            
        return
    
    dfs(start, roads)
    
    if len(result) >0:
        answer = min(result)
    return answer