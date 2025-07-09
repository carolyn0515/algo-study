import sys
input = sys.stdin.readline

output = []
while True:
    line = input().rstrip()
    if line == '.':  
        break
    stack = []
    balanced = True
    for char in line:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                balanced = False
                break
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                balanced = False
                break
    if balanced and not stack:
        output.append("yes")
    else:
        output.append("no")

print('\n'.join(output))
