'''
Array
'''

def solution(fees, records):
    answer = []
    notOutCarNum = []
    carTimeDict = {} # carNumber : [sumTime, timeLog]
    endTime = '23:59'
    baseTime, basePay, addTime, addPay = fees

    def calcPay(time):
        if time <= baseTime:
            return basePay
        carAddTime = time - baseTime
        if carAddTime % addTime == 0:
            carAddPay = int(carAddTime / addTime) * addPay
        else:
            carAddPay = (int(carAddTime / addTime) + 1) * addPay
        return carAddPay + basePay

    def calcTime(inTime, outTime):
        resultMin = 0
        inHour, inMin = map(int, inTime.split(":"))
        outHour, outMin = map(int, outTime.split(":"))
        
        if outMin - inMin > 0:
            resultMin += outMin - inMin
            resultMin += (outHour - inHour) * 60
        else:
            resultMin += outMin + (60 - inMin)
            resultMin += (outHour - inHour - 1) * 60
        
        return resultMin
    
    for log in records:
        carTime, carNum, carInOut = log.split()
        if carNum not in carTimeDict.keys():
            carTimeDict[carNum] = [0, ""]
        
        if carInOut == 'OUT':
            carTimeDict[carNum][0] += calcTime(carTimeDict[carNum][1], carTime)
            carTimeDict[carNum][1] = ''
            notOutCarNum.remove(carNum)
        else:
            carTimeDict[carNum][1] = carTime
            notOutCarNum.append(carNum)

    for carNum in notOutCarNum:
        carTimeDict[carNum][0] += calcTime(carTimeDict[carNum][1], endTime)

    for car in sorted(carTimeDict.keys()):
        answer.append(calcPay(carTimeDict[car][0]))
            
    # 오름차순 정렬
    return answer