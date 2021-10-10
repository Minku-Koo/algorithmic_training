


def solution(info, edges):
    
    answer = 0
    # 이진트리 딕셔너리
    tree = {}
    animals = {'sheep':1,'fox':0}
    
    
    # -------------------
    for e in edges: 
        tree[ e[1] ] = []
        tree[ e[0] ] = []
        
    for e in edges:
        if e[0] not in tree: 
            tree[ int(e[0]) ] = [e[1]]
        else: tree[int(e[0])].append(e[1])
    #return tree
    
    
    def get_paths(s, target, c = []):
        if not tree[s]:
            yield c+[s]
        elif s == target:
            yield c+[s]
        else:
            for i in tree[s]:
                yield from get_paths(i, target, c+[s])
    
    
    
    # =-================
    # 양까지 늑대 몇마리인지 계산
    def countFox(disc):
        count  = 0
        for d in disc:
            if info[d] == 1: count+=1
            #count += info[d]
        return count # 늑대 총 개수
    # --=-=-=-=-=---------------
    root = 0 # 현위치
    while True:
        # 모든 양중에서 늑대 가장 적은놈
        min_indx, min_fox, min_path = 0, 9999, []
        is_shp = False
        for idx, shp in enumerate(info):
            if idx == root: continue
            if shp == 0: #양인 경우
                is_shp = True
                newpath = list( get_paths(0, idx) )
                print("타겟은",idx)
                print("전체경로는",newpath)
                for pat in newpath:
                    if idx in pat:
                        path = pat
                        break
                #return path
                print("좋은패스:",path)
                fox_count = countFox(path)
                #return newpath
                if fox_count < min_fox: #늑대 가장 적은 놈 갱신
                    min_indx =  idx
                    min_fox = fox_count
                    min_path = path
                    #return root, idx, 999,  min_fox,  min_path
        
        # 노드 이동
        # 늑대가 더많으면 종료
        
        if animals['sheep'] <= animals['fox'] + min_fox:
            print("---can eat")
            print("root min_path/", min_path)
            print("animals", animals )
            break
        
        root = min_indx # root 갱신
        animals['sheep'] += 1 # 양 갱신
        animals['fox'] += min_fox # 늑대 갱신
        print("animals", animals)
        print("path", min_path)
        for p in min_path:
            info[p] = -2
        print("info >>", info)
        # 종료 판단 : 양 없는 경우
        if info.count(0) == 0:
            print("yang no")
            break
            
        
    answer = animals['sheep']
    
    
    return answer


if __name__ == "__main__":
    info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
    edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]

    print(solution(info, edges) ) 