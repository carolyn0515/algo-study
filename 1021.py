import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dq = deque(range(1, n + 1))  # 1부터 시작해야 함
targets = list(map(int, input().split()))
count = 0

for target in targets:
    idx = dq.index(target)
    if idx <= len(dq) // 2:
        # 왼쪽으로 돌리는 게 더 적음
        for _ in range(idx):
            dq.append(dq.popleft())
            count += 1
    else:
        # 오른쪽으로 돌리는 게 더 적음
        for _ in range(len(dq) - idx):
            dq.appendleft(dq.pop())
            count += 1
    dq.popleft()  # 목표 숫자 제거 (이건 count 안함)

print(count)
