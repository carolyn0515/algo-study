import sys 
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in  range(n)]
dx = [-1, 1, 0, 0] # up down left right
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or  nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
bfs(0,0)
print(maze[n-1][m-1])
# DFS는 경로는 찾지만, 최단을 보당하지는 않는다
# BFS는 레벨 탐색 -> 먼 거리부터 가까운 거리까지 차례로 탐색 