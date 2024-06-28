posStr = input() # 열, 행 순서

colToint = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

x = colToint[posStr[0]]
y = int(posStr[1])

initX, initY = x, y

d1x = [1, -1]
d2x = [2, -2]
d1y = [1, -1]
d2y = [2, -2]

count = 0

# 수평 먼저
for dx in d2x:
    x, y = initX, initY

    x += dx
    if x < 1 or x > 8:
        continue
    else:
        for dy in d1y:
            y = initY

            y += dy
            if y < 1 or y > 8:
                continue
            else:
                count += 1
                print(f"dx:{dx}, dy:{dy}, x:{x}, y:{y}")

# 수직 먼저
for dy in d2y:
    x, y = initX, initY

    y += dy
    if y < 1 or y > 8:
        continue
    else:
        for dx in d1x:
            x = initX
            x += dx
            if x < 1 or x > 8:
                continue
            else:
                count += 1
                print(f"dx:{dx}, dy:{dy}, x:{x}, y:{y}")

print(count)
