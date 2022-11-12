'''
Hashing
'''
import collections
def solution(id_list, report, k):
    answer = []

    # 중복 제거
    report = set(report) 
    # 신고당한 횟수
    reportCount = collections.defaultdict(int) 
    # 신고한 사람 : 신고당한 사람 이름 리스트
    history = collections.defaultdict(list)

    for cmd in report:
        # cmd : string, split by space
        name, target = cmd.split()
        reportCount[target] += 1
        history[name].append(target)

    for id in id_list:
        count = 0 # mail count
        # 자신이 메일 받을 횟수 계산하기 위한 loop
        for target in history[id]:
            # k 이상 신고당한 경우만 count 증가
            if reportCount[target] >= k:
                count += 1
        
        answer.append(count)

    return answer