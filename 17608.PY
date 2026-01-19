import sys

data = sys.stdin.buffer.read().split()
n = int(data[0])

M = -10**18
count = 0

for i in range(n, 0, -1):
    x = int(data[i])
    if x > M:
        M = x
        count += 1

print(count)
