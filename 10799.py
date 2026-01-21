list = list(input().strip())
stack = [1 if x == ")" else -1 if x == "(" else x for x in list]
sum = 0
total = 0
flag = 0
while(stack):
    x = stack.pop()
    sum += x
    if x ==1:
        flag = 1
    else: 
        if (flag == 1): total += sum
        else: total += 1
        flag = 0
print(total)