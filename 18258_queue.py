from collections import deque
import sys 
input = sys.stdin.readline
output = []

n = int(input())
queue = deque()

for _ in range(n):
    command = input().strip()
    if command.startswith("push"): queue.append(int(command.split()[1]))
    elif command.startswith("pop"): output.append(queue.popleft() if queue else "-1")
    elif command.startswith("size"): output.append(str(len(queue)))
    elif command.startswith("empty"): output.append("0" if queue else "1") # if queue: queue가 비어있지 않으면 T else F
    elif command.startswith("front"): output.append(queue[0] if queue else "-1")
    elif command.startswith("back"): output.append(queue[-1] if queue else "-1")
    else: break
print("\n".join(map(str, output)))