s = input().strip()
if len(s) == 1:
    s = "0" + s

a = list(s)
first = 10*int(a[0]) + int(a[1])

sub = first//10 + first%10
n = 0
new = -1  # 0 입력 케이스 방지용

while new != first:
    if n == 0:
        sub %= 10
        new = first%10*10 + sub
    else:
        sub = (new//10 + new%10) % 10
        new = new%10*10 + sub
    n += 1

print(n)
