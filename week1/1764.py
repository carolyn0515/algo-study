import sys

input = sys.stdin.readline
n, m = map(int, input().split())
li = []

for _ in range(n):
    li.append(input().strip()) 

for _ in range(m):
    li.append(input().strip())

from collections import Counter

li_counter = Counter(li)

ans = [name for name, cnt in li_counter.items() if cnt == 2]
ans.sort()

print(len(ans))
print("\n".join(ans))
