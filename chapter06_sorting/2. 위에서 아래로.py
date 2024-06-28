n = int(input())
numbers = []

for i in range(n):
    num = int(input)
    numbers.append(num)

numbers = sorted(numbers, reverse=True)

for i in numbers:
    print(i, end=' ')