def recursiveBinarySearch(arr, target, start, end): # 찾고자 하는 원소의 인덱스 반환
    if start > end:
        return None
    
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recursiveBinarySearch(arr, target, start, mid - 1)
    else:
        return recursiveBinarySearch(arr, target, mid + 1, end)
    
def iterativeBinarySearch(arr, target, start, end):

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


n, target = map(int, input().split())
arr = list(map(int, input().split()))

# result = recursiveBinarySearch(arr, target, 0, n - 1)
result = iterativeBinarySearch(arr, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(f"{result}번째 인덱스에 원소가 존재합니다.")