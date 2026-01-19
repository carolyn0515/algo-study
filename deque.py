from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dq = deque()
output = []

for _ in range(n):
    cmd = input().strip().split()

    if cmd[0] == 'push_front':
        dq.appendleft(int(cmd[1]))
    elif cmd[0] == 'push_back':
        dq.append(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        output.append(str(dq.popleft()) if dq else '-1')
    elif cmd[0] == 'pop_back':
        output.append(str(dq.pop()) if dq else '-1')
    elif cmd[0] == 'size':
        output.append(str(len(dq)))
    elif cmd[0] == 'empty':
        output.append('0' if dq else '1')
    elif cmd[0] == 'front':
        output.append(str(dq[0]) if dq else '-1')
    elif cmd[0] == 'back':
        output.append(str(dq[-1]) if dq else '-1')

print("\n".join(output))
