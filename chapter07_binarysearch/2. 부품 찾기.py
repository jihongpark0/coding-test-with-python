import sys

def recursiveBinarySearch(arr, target, start, end): # 찾고자 하는 원소의 인덱스 반환
    if start > end: # arr이라는 list내에서 target을 발견하지 못했을 경우, None 반환
        return None
    
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recursiveBinarySearch(arr, target, start, mid - 1)
    else:
        return recursiveBinarySearch(arr, target, mid + 1, end)

n = int(input())
parts = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
req = list(map(int, sys.stdin.readline().rstrip().split()))

parts.sort()
for r in req:
    if recursiveBinarySearch(parts, r, 0, n - 1) == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
