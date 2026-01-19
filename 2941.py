a = input()
li = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for x in li:
    a = a.replace(x, "*")

print(len(a))