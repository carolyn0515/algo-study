n = int(input())
for i in range(n):
    ans = []
    a = list(input())
    ans.append(a[0])
    ans.append(a[-1])
    print("".join(ans))