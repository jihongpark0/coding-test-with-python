n = int(input())
array = list(map(int, input().split()))

d = [0] * 30001

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n): # n은 array의 길이이므로 
    d[i] = max()    
