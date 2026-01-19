save = [[0]*9 for _ in range(9)]
keys = []
values = []
for i in range(9):
    a = list(map(int, input().split()))
    save[i] = a
    b = max(a)
    location = (i, a.index(b))
    keys.append(location)
    values.append(b)
c = max(values)
loc = values.index(c)
max_lo = keys[loc]
print(c)
print(str(max_lo[0]+1) + " " + str(max_lo[1]+1))