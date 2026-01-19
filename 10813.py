n, m = map(int, input().split())
d = [(i, v) for i, v in enumerate(range(1, n+1))]
for i in range(m):
    p, q = map(int, input().split())
    blank = 0
    blank = d[p-1]
    d[p-1] = d[q-1]
    d[q-1] = blank
for i in range(n): print(d[i][1], end=" ")
