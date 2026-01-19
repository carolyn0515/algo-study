num, law = map(int, input().split())
ans = []

def val_to_char(v):
    if 0 <= v <= 9:
        return chr(v + ord('0'))
    else:
        return chr(v - 10 + ord('A'))

while num > 0:
    left = num % law
    ans.append(val_to_char(left))
    num //= law

print(''.join(reversed(ans)))
