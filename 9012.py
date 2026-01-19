import sys
input = sys.stdin.readline

n = int(input())
output = []

for _ in range(n):
    s = input().strip()
    stack = []  # 매 테스트케이스마다 새로 초기화

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                output.append("NO")
                break
    else:
        # for문이 break 없이 정상 종료된 경우
        if not stack:
            output.append("YES")
        else:
            output.append("NO")

print("\n".join(output))
