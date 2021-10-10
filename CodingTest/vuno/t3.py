# 입력
# 입력
interval = []
loop = int(input())
time_limit = 0
for _ in range(loop):
	line = [int(k) for k in input().split()]
	time_limit = max(line) if max(line) > time_limit else time_limit
	interval.append(line)

work_time = [i for i in range(1,time_limit+1 )]
for itv in interval:
	for t in range(itv[0]):
		
		for work in range(itv[2*t +1], itv[2*t +2]):
            
			if work in work_time: work_time.remove(work)
result = 0
for i, w in enumerate(work_time):
	if i==0: continue
	if w - work_time[i-1] > 1:
		result +=1
        
print(result)