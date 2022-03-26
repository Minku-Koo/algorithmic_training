#

from itertools import combinations 
arr = list(map(int, input().split()))

result = []
for i in range(1, 11):
  result = result+list(combinations(arr,i))  

for r in result:
    if 0==sum(r):
        print(r)
