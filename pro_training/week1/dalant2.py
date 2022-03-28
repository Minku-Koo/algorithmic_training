T=int(input())
for tc in range(1,T+1):
    d,c=list(map(int,input().split())); r=1
    for i in [d//c for _ in range((c-d%c))]+[d//c+1 for _ in range(d%c)]:r*=i
    print(f"#{tc} {r}")

#1 36
#2 1024
#3 46656
#4 1679616
#5 26214400
#6 2448880128
#7 125524238436
#8 2821109907456
#9 162679413013056
#10 5856458868470016


