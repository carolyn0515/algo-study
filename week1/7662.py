import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    min_h = []
    max_h = []
    visited = [False] * k  

    for i in range(k):
        op, num = input().split()
        num = int(num)

        if op == 'I':
            heapq.heappush(min_h, (num, i))    
            heapq.heappush(max_h, (-num, i))    
            visited[i] = True                  

        elif op == 'D':
            if num == 1:
                while max_h and not visited[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    visited[max_h[0][1]] = False
                    heapq.heappop(max_h)

            else:
                while min_h and not visited[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    visited[min_h[0][1]] = False
                    heapq.heappop(min_h)

    while min_h and not visited[min_h[0][1]]:
        heapq.heappop(min_h)
    while max_h and not visited[max_h[0][1]]:
        heapq.heappop(max_h)

    if not min_h or not max_h:
        print("EMPTY")
    else:
        print(f"{-max_h[0][0]} {min_h[0][0]}")