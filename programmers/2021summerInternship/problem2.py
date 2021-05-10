# 21.05.09

def solution(t, r):
    answer = []
    indexs = [x for x in range(len(t))]
    time = 0
    while len(answer)< len(t):
        cnt = t.count(time)
        

        if cnt>0:
            if cnt ==1:
                ind = t.index(time)
                answer.append(ind)
            else:
                tlist = []
                for ind, tt in enumerate(t):
                    if tt == time:
                        tlist.append( [  r[ind], ind ]  )
                slist = sorted(tlist, key=lambda x:(x[0], x[1]) )
                answer.append( slist[0][1] )
                for s in slist[1:]:
                    t[s[1]] += 1
        time+=1
        
    
    return answer