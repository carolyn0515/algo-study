import sys, heapq
input = sys.stdin.readline
output = []

T = int(input())
for _ in range(T):
    hq = []
    J, N = map(int, input().split())
    for _ in range(N):
        R, C = map(int, input().split())
        heapq.heappush(hq, -(R * C)) 

    total = 0
    count = 0
    while total < J:
        total += -heapq.heappop(hq)
        count += 1

    output.append(count)

print('\n'.join(map(str, output)))
