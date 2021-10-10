# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# BFS
# https://www.acmicpc.net/problem/1697
from collections import deque
n, k = list(map(int, input().split()))

# BFS 이용한 탐색
def bfs(n, k):
	visit = [0]*100001
	queue = deque([n] )

	if n>k:
		return n-k

	while queue:
		p = queue.popleft()
		if p == k: return visit[p] # 동생을 찾으면 단계 반환
		
		
		tmp = visit[p]
		if  p<100000 and visit[p+1] ==0: 
			queue.append(p+1)
			visit[p+1] = tmp+1
			
		if p>0 and visit[p-1]==0:
			queue.append(p-1)
			visit[p-1] = tmp+1
			
		if  p<=50000 and visit[p*2]==0: 
			queue.append(p*2)
			visit[p*2] = tmp+1
		
print(bfs(n, k))

