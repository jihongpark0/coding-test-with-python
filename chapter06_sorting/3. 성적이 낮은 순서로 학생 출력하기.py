n = int(input())
students = []

for i in range(n):
    l = input().split(' ')
    name = l[0]
    score = int(l[1])
    students.append((name, score))

l = sorted(students, key=lambda item: item[1])

for i in l:
    print(i[0], end=' ')
    

