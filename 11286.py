import heapq, sys
input = sys.stdin.readline

hq = []
output = []

n = int(input())
for _ in range(n):
    a = int(input())
    if a == 0:
        if hq:
            output.append(str(heapq.heappop(hq)[1]))
        else:
            output.append("0")
    else:
        heapq.heappush(hq, (abs(a), a))

print('\n'.join(output))
