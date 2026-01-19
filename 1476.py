E, M, S = map(int, input().split())

y = 1
while True:
    if (y - E) % 15 == 0 and (y - M) % 28 == 0 and (y - S) % 19 == 0:
        print(y)
        break
    y += 1
