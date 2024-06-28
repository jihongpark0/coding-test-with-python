n = int(input("N: "))
x, y = 1, 1
plans = input("plans: ").split()

for p in plans:
    if p == "U":
        y -= 1
    elif p == "D":
        y += 1
    elif p == "L":
        x -= 1
    elif p == "R":
        x += 1

    if x > n:
        x -= 1
    elif y > n:
        y -= 1

    if x < 1:
        x = 1
    elif y < 1:
        y = 1

    print(x, y)

print(x, y)









