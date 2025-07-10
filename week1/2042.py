import sys
input = sys.stdin.readline

def init(start, end, node):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return tree[node]

def update(start, end, node, idx, diff):
    if idx < start or idx > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(start, mid, node*2, idx, diff)
        update(mid+1, end, node*2+1, idx, diff)

def query(start, end, node, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(start, mid, node*2, left, right) + query(mid+1, end, node*2+1, left, right)

n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
tree = [0] * (n * 4)

init(0, n-1, 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        diff = c - nums[b]
        nums[b] = c
        update(0, n-1, 1, b, diff)
    else:
        print(query(0, n-1, 1, b-1, c-1))
