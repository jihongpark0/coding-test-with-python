# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# n: 배열의 크기
# m: 총 더해지는 횟수
# k: k번까지 같은 인덱스의 요소 연속 덧셈 가능

# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

# print(f"{n} {m} {k}")
# print(data)

# 첫번째 큰 수 찾기
first_index = 0
first = data[0]
for i in range(1, n):
    if first < data[i]:
        first = data[i]
        first_index = i
print(f"첫번째 큰 수: {first}")

# 두번째 큰 수 찾기
second = -1
for i in range(n):
    if i == first_index:
        continue
    if second < data[i]:
        second = data[i]
print(f"두번째 큰 수: {second}")

# 구하기
k_counter = 0
s = 0
for _ in range(m):
    if k_counter < k:
        s += first
        k_counter += 1
        print(first)
    else:
        k_counter = 0
        s += second
        print(second)

print(s)










