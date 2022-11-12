'''
Array
'''

def solution(fees, records):
    answer = []
    notOutCarNum = []
    carTimeDict = {} # carNumber : [(int)sumTime, (str)IN time]
    endTime = '23:59'
    baseTime, basePay, addTime, addPay = fees

    # min 시간 입력 -> 금액 계산
    def calcPay(time):
        if time <= baseTime:
            return basePay
        carAddTime = time - baseTime
        if carAddTime % addTime == 0:
            carAddPay = int(carAddTime / addTime) * addPay
        else:
            carAddPay = (int(carAddTime / addTime) + 1) * addPay
        return carAddPay + basePay

    # str IN OUT 입력 -> int 시간 계산 (min)
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
            # 주차장에 남아있는 차량 번호 삭제
            notOutCarNum.remove(carNum)
        else:
            carTimeDict[carNum][1] = carTime
            # 주차장에 남아있는 차량 번호 추가
            notOutCarNum.append(carNum)

    for carNum in notOutCarNum:
        # 남아있는 차량은 end time으로 시간 계산
        carTimeDict[carNum][0] += calcTime(carTimeDict[carNum][1], endTime)

    for car in sorted(carTimeDict.keys()):
        # 차량 번호로 오름차순 및 요금 계산
        answer.append(calcPay(carTimeDict[car][0]))
            
    return answer