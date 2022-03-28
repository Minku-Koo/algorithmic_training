
def quick(arr):
    if len(arr) <= 1: return arr
    
    pivot, nums = arr[0], arr[1:]
    
    left = [x for x in nums if x <= pivot]
    right = [x for x in nums if x > pivot]
    
    return quick(left) + [pivot] + quick(right)

def merge(arr):
    if len(arr) < 2: return arr

    center = len(arr) // 2
    low = merge(arr[:center])
    high = merge(arr[center:])

    merge_arr = []
    l = h = 0
    while l < len(low) and h < len(high):
        if low[l] < high[h]:
            merge_arr.append(low[l])
            l += 1
        else:
            merge_arr.append(high[h])
            h += 1
    merge_arr += low[l:]
    merge_arr += high[h:]
    return merge_arr