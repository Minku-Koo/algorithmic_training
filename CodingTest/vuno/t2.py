
# 입력값
width = int(input())
graph = [ list(map(int, input().split())) for _ in range(2 * (width-1) + 1) ]

# BFS
stack = [[0, 0]]
visit = []
answer, loc = [], [0, 0]

def dfs(graph, loc, visit=[]):
	visit.append(loc)
	
	new_loc = []
	if loc[0] == 2 * (width) :
		answer.append( visit[:-1] )
		return visit[:]
	#다이아몬드 아래쪽
	elif loc[0] > width-1:
		if loc[1] == 0:
			new_loc.append( ( loc[0]+1, loc[1] ) )
		elif loc[1] == len(graph[loc[0]])-1:
			new_loc.append( (  loc[0]+1, loc[1]-1 )  )
		else:
			new_loc.append( (  loc[0]+1, loc[1]) )
			new_loc.append( (  loc[0]+1, loc[1]-1 ) )

	else: # 다이아몬드 위쪽
		new_loc.append( ( loc[0]+1, loc[1] ) )
		new_loc.append( ( loc[0]+1, loc[1]+1 ) )
			
	for start in new_loc:
		dfs(graph, start, visit)
		visit.pop()
			
	return visit


dfs(graph, (0, 0))
ansum = []
for ans in answer:
	print("ans>",ans)
	ansum.append( sum( [graph[k[0]][k[1]] for k in ans] ) )

result = max(ansum)


print(result)

