#



def solution( root, edge, r1, r2, tree ):
    btree = {}
    utree = {}
    for j in range(len(tree)-1):
        if j%2==1: continue
        pr, ch =  tree[j], tree[j+1]
        btree[pr] = btree.get(pr, [])
        btree[pr].append(ch)
        
        utree[ch] = pr
    
    def get_root(node, base = []):
        root = [1]
        while node!=1:
            if base:
                if node in base: return [node], True
            root.append(node)
            node = utree[node]
        return  root, False
    
    base, _ = get_root(r1)
    master, _ = get_root(r2, base)
    # master = list( set(get_root(r1)) & set(get_root(r2)) )[-1]
    
    q = [master[0]]
    cnt = 0
    while q:
        qnode = q.pop(0)
        cnt+=1
        if not btree.get(qnode): continue
        for j in btree[qnode]:
            q.append(j)
            
    return master[0], cnt

T=int(input())
for tc in range(1,T+1):
    root, edge, r1, r2 =list(map(int,input().split()))
    tree =list(map(int,input().split()))
    root_node, node_count = solution( root, edge, r1, r2, tree )
    print(f"#{tc} {root_node} {node_count}")

#1 3 8
#2 1 10
#3 21 35
#4 1 100
#5 168 107
#6 1 500
#7 398 840
#8 747 1359
#9 498 3141
#10 7165 2435
