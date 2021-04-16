# 21.04.17
# p.355
# Problem Title : 부분 집합

def solution(plans):
    result = []
    root = []

    def dfs(start, plan):
        if len(plans) == len(root):
            result.append(root[:])
            return

        for p in plan:
            if p[0] == start[1]:
                root.append(p)
                newPlan = plan[:]
                newPlan.remove(p)
                dfs(p, newPlan)
                root.pop()
        
        return

    for point in plans:
        if point[0] == "J":
            root.append(point)
            newPlan = plans[:]
            newPlan.remove(point)
            dfs(point, newPlan)
            root = []
    
    result = sorted(result, key = lambda x : x[0])[0]
    sortedResult = [ result[0][0] ]
    
    for r in result:
        sortedResult.append( r[1] )
        
    return sortedResult


if __name__ == "__main__":
    plans = [ ["J", "S"], ["J", "A"], ["S", "A"], ["A", "J"], ["A", "S"] ]
    result = solution(plans)
    print("result:", result)


