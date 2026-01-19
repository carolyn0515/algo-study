n = int(input())
li = list(map(int, input().split()))

st = 0
ans = []
f = 0

def step():
    global st, f
    if f + 2 >= n:
        return

    if (li[f] < li[f+1]) and (li[f+1] < li[f+2]):
        st = f
        last = f + 2
        f += 2

        while (last + 1 < n) and (li[last + 1] < li[last]):
            last += 1

        ans.append(li[last] - li[st])

while f < n - 2:
    step()
    f += 1  # 안전하게라도 전진 (무한루프 방지)

print(max(ans) if ans else 0)
