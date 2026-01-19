import sys
sys.setrecursionlimit(10**6)  

input = sys.stdin.readline

n = int(input()) 
tree = [[] for _ in range(n+1)]  

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)  

parent = [0] * (n+1)
visited = [False] * (n+1)

def dfs(current):
    visited[current] = True  
    for next in tree[current]:  
        if not visited[next]:  
            parent[next] = current  
            dfs(next)  

dfs(1)

for i in range(2, n+1):
    print(parent[i])
