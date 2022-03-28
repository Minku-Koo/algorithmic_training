#

def check(baby):
    same = 11
    for k in range(10):
        if list(baby).count(str(k))>=3:
            same = k
            break
    if same==11: return False
    
    arr  = list(map(int, baby))
    for _ in range(3): arr.remove(same)
    arr = sorted(arr)
    if arr[1]+1==arr[2] and arr[2]-2==arr[0]: return True
        
    return False

if __name__ == "__main__":
    s = input()
    print(check(s))