li = []
for i in range(9):
    li.append(int(input()))
li.sort()
sum = sum(li)
left = sum - 100
m = 0
M = -1
min = li[m]
max = li[M]
while (min + max) != left:
    if (min + max) > left:
        M -= 1
        max = li[M]
    else:
        m += 1
        min = li[m]
li.remove(min)
li.remove(max)
for i in li:
    print(i)