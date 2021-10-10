#

n = int(input())
layers = [ int(value) for value in input().split() ]

answer = sum([j*layers[index-1] if index!=0 else 0 for index, j in enumerate(layers)  ])

print(answer)