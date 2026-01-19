li = [[None]*15 for _ in range(5)]
for a,b in enumerate(li):
    li[a] = list(input())
ans = []
for j in range(5):
    for i in range(5):
        if li[i][j] is not None:
            ans.append(li[i][j])
print("".join(ans))