s = input()

group = 0
gc = [0, 0]

if s[0] == '0':
    gc[0] += 1
else:
    gc[1] += 1
    group = 1

for i in range(1, len(s)):
    if int(s[i]) != group:
        group = int(s[i])
        gc[group] += 1

print(min(gc))