import sys
from collections import Counter
input = sys.stdin.readline
output = []
T = int(input())

for _ in range(T):
    n = int(input())
    counter = Counter()
    
    for _ in range(n):
        name, kind = input().strip().split()
        counter[kind] += 1
    
    result = 1
    for cnt in counter.values(): # values쓰면 각 keky에 대응하는 개수들만 리스트처럼 반환해줌 
        result *= (cnt + 1)  # 안 입는 경우 포함
    
    output.append(str(result - 1))  # 아무것도 안 입는 경우 제외

print("\n".join(output))

