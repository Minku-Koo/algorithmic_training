
# F = G * m1 * m2 / (d*d)
# 소수점 10번째까지 출력
def solution( count, info ) :
    x_coords, weight = info[:count], info[count:]
    result = []
    def getPower(x_coords, weight, pos):
        left, right = 0.0, 0.0
        for idx, x in enumerate(x_coords):
            if x==pos: continue
            
            if x < pos: left += weight[idx] / abs( x - pos ) **2
            else: right += weight[idx] / ( x - pos ) **2
        return left, right
    
    
    for i in range( count-1 ):
        start, end = round((x_coords[i]+x_coords[i+1])/2, 2), x_coords[i+1]
        org_start, org_end = x_coords[i], end
        moc= 1/10
        
        lside, rside = getPower(x_coords, weight, start)
        status = 0 if lside>rside else 1
        while (lside != rside):
            temp = start
            lside, rside = getPower(x_coords, weight, start)
            change = 0 if lside>rside else 1
            
            if change==0:
                start += moc
            else: 
                start -= moc
            
            if start < org_start:
                start += moc
                moc *= 0.1
            if start > org_end:
                start -= moc
                moc *= 0.1
            
            if change!=status:
                moc *= 0.1
                status = change
            
            if abs(lside - rside) < 0.1**5 and start == temp: 
                break
            
            if abs(lside - rside) < 0.1**12:
                break
        
        result.append( round(start, 10) )
        pass
    
    
    return result



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    count = int(input())
    info = list(map( int, input().split() ))
    print("#"+str(test_case), end=' ')
    result = solution( count, info )
    for r in result:
        print( "%.10f" %r , end=" ")


#1 1.5000000000
#2 1.0306534300
#3 462.5504629633
#4 1.4060952085 2.5939047915
#5 2.5328594461 3.7271944335 6.0999536409
#6 6.3428568767 11.5477377494 15.9641592998 24.9267991615
#7 57.8805685415 81.8651598883 91.0573691382 105.0835650491 133.2934094881
#8 74.2211477711 190.6837563313 305.8269181686 348.3304429927 470.2694219293 555.4943093854
#9 21.5171374463 47.9890597763 68.6536668433 82.9131954023 95.0052272762 99.1999097770 116.4978330953
#10 11.5573600056 24.0238341337 38.4847676134 44.6137453708 64.7500445424 126.9908128982 184.3221650927 197.9760596291 266.0574653677
