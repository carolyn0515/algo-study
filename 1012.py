from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    queue = deque()
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
        queue.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    count = 0

    while queue:
        x, y = queue.popleft()
        if visited[y][x]:
            continue  
        visited[y][x] = True
        bfs_q = deque()
        bfs_q.append((x, y))

        while bfs_q:
            cx, cy = bfs_q.popleft()
            for d in range(4):
                nx = cx + dx[d]
                ny = cy + dy[d]
                if 0 <= nx < M and 0 <= ny < N:
                    if field[ny][nx] == 1 and not visited[ny][nx]:
                        visited[ny][nx] = True
                        bfs_q.append((nx, ny))
        
        count += 1 

    print(count)
