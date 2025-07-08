# 1번 카드가 젤 위에, N이 젤 아래
# 1장 남을 떄까지 제일 위 카드 바닥에 버림, 그 다음 위의 카드를 가장 밑으로 옮김

from collections import deque
import sys 
input = sys.stdin.readline
n = int(input())
q = deque(range(1, n+1))
while len(q) > 1: 
    q.popleft()              # 1. 제일 위 카드 버림
    q.append(q.popleft())    # 2. 그 다음 카드를 밑으로 보냄
print(q[0])  # 마지막 남은 카드 출력