def currentVal(ds, mid):
    s = 0
    for d in ds:
        left = d - mid
        if left > 0:
            s += left

    return s

n, m = map(int, input().split()) # n: 떡의 갯수, m: 요청한 떡의 길이
ds = list(map(int, input().split()))

start = 0
end = max(ds) - 1 # 떡의 길이 중 가장 긴 것
mid = (start + end) // 2

while start <= end:
    s = currentVal(ds, mid)
    if s == m:
        break
    elif s < m:
        end = mid - 1
    else:
        start = mid + 1
    mid = (start + end) // 2
    
print(mid)