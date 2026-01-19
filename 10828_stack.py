import sys
input = sys.stdin.readline

stack = []
top = -1 
output = []

def push(a):
    global stack, top
    top += 1 
    stack.append(a)

def pop():
    global stack, top
    if top == -1:
        output.append("-1")
    else: 
        output.append(str(stack[top]))
        stack.pop()
        top -= 1 
num = int(input())
for _ in range(num):
    command = input().strip()
    if command.startswith("push"):
        push(int(command.split()[1]))
    elif command == "pop": pop()
    elif command == "top": output.append("-1" if top == -1 else str(stack[top]))
    elif command == "size": output.append(str(stack[top]))
    elif command == "size": output.append(str(top + 1))
    elif command == "empty": output.append("1" if top == -1 else "0")