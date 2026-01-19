import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited_dfs = [False] * (n+1)

def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    for u in graph[v]:
        if not visited_dfs[u]:
            dfs(u)
# 일단 현위치 True로 바꾸고
# 출력 때리고
# 현위치랑 이어진 노드 돌면서 
# 아직 안 방문했던 애 있으면 재귀 
# 그렇게 쭉쭉 내려가는겨 

visited_bfs = [False] * (n+1)

def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for u in graph[v]:
            if not visited_bfs[u]:
                visited_bfs[u] = True
                queue.append(u)
# queue에 지금 애 담아
# 지금 애 위치 True로 바꾸고
# 큐에 뭔가가 있을 때
# 왼쪽부터 튀어나가서 출력하는겨 (옆으로 탐색하는 애니까 왼쪽부터인겨)
# 지금 애 밑에 딸린 안 방문했던 애 있으면 방문 표시하고 큐에 담아. 
# 그러면 지금 애 라인에 있던 애들 쫙 출력하고 나서 
# 그 밑에 애들 (아까 담아두었던 것들) 쫙 돌겠지
# 그렇게 하나씩 내려가면서 왼쪽 부터 쭈우욱 출력 

dfs(v)
print()
bfs(v)
