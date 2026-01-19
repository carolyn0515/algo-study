from collections import Counter
dice = list(map(int, input().split()))
cnt = Counter(dice)
if 3 in cnt.values():
    k = [key for key,val in cnt.items() if val == 3][0]
    print(10000 + k*1000)
elif 2 in cnt.values():
    k = [key for key,val in cnt.items() if val == 2][0]
    print(1000 + k*100)
else:
    print(max(dice)*100)
