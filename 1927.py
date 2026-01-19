import heapq
import sys

input = sys.stdin.readline
hq = []
output = []

n = int(input())
for _ in range(n):
    a = int(input())
    if a == 0:
        if len(hq) == 0:
            output.append('0')
        else:
            output.append(str(heapq.heappop(hq)))
    else:
        heapq.heappush(hq, a)

print('\n'.join(output))
