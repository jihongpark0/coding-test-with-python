n = int(input()) # n: 모험가의 수
member = list(map(int, input().split()))

member.sort()
member = [0] + member

lpi = 0 # last pop index: 마지막으로 그룹을 형성시킨 인덱스
gc = 0 # group counter: 형성된 그룹의 수

for i in range(1, n + 1):
    if i - lpi == member[i]:
        gc += 1
        lpi = i

print(gc)

