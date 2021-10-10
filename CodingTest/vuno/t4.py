h, w = map(int, input().split())
box = []
for _ in range(h):
	line = list(map(int, input().split()))
	box.append(line)

def bfs(box, y, x):
	visited = []
	queue = [(y, x)]

	while queue:
		n = queue.pop(0)
		if n in visited: continue
			
		if n[0]>0 and box[n[0]-1][n[1]]==1:
			queue.append( (n[0]-1, n[1]) )
		if n[0]<h-1 and box[n[0]+1][n[1]]==1:
			queue.append( (n[0]+1, n[1]) )
		if n[1]<w-1 and box[n[0]][n[1]+1]==1:
			queue.append( (n[0], n[1]+1) )
		if n[1]>0 and box[n[0]][n[1]-1]==1:
			queue.append( (n[0], n[1]-1) )
		
		visited.append(n)
		
			
	return visited
	
#
result = 0
for y in range(h):
	for x in range(w):
		if box[y][x] == 1:
			#print(y, x)
			pos = bfs(box, y, x)
			#print(pos)
			xlist, ylist = [],[]
			for p in pos:
				box[p[0]][p[1]] = 0
				xlist.append(p[1])
				ylist.append(p[0])
			print(pos)
			result += (max(xlist)-min( xlist )+1) * (max(ylist)-min( ylist )+1)
			
			
			
print(result)