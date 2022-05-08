# n : 수의 개수, m : 수의 변경이 일어나는 횟수, k : 구간의 합을 구하는 횟수
from math import log2, ceil
from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
h = int(ceil(log2(n)))
t_size = 1 << (h + 1)
tree = [0 for i in range(t_size)]
lst = []
operator = deque()
for i in range(n):
    lst.append(int(input()))

for i in range(m + k):
    operator.append(list(map(int, input().split())))


def make_segment(start, end, index):
    if start is end:
        tree[index] = lst[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = make_segment(start, mid, index*2) + make_segment(mid + 1, end, index*2 + 1)
    return tree[index]


def query(start, end, index, query_left, query_right):
    if query_left > end or query_right < start:
        return 0
    if query_left <= start and end <= query_right:
        return tree[index]
    mid = (start + end) // 2
    return query(start, mid, index*2, query_left, query_right) + query(mid + 1, end, index*2 + 1, query_left, query_right)


def update(new_idx, diff, index, update_left, update_right):
    if new_idx < update_left or update_right < new_idx:
        return
    tree[index] += diff
    if update_right is not update_left:
        mid = (update_left + update_right) // 2
        update(new_idx, diff, index*2, update_left, mid)
        update(new_idx, diff, index*2+1, mid+1, update_right)
####################################################################
# def update(new_idx, new_val, index, update_left, update_right):
#     if new_idx < update_left or update_right < new_idx:
#         return tree[index]
#     if update_right is update_left:
#         tree[index] = new_val
#         return tree[index]
#     mid = (update_left + update_right) // 2
#     tree[index] = update(new_idx, new_val, index*2, update_left, mid) + update(new_idx, new_val, index*2+1, mid+1, update_right)
#     return tree[index]
####################################################################

make_segment(0, n-1, 1)
while operator:
    oper = operator.popleft()
    if oper[0] == 1:
        # 원래 리스트의 값과 바꿔주려는 값의 차이 값
        diff = oper[2] - lst[oper[1] - 1]
        # 원래 리스트를 바꿔줌
        lst[oper[1] - 1] = oper[2]
        update(oper[1]-1, diff, 1, 0, n-1)
    else:
        print(query(0, n-1, 1, oper[1]-1, oper[2]-1))

# 5 2 2
# 1
# 2
# 3
# 4
# 5
# 1 3 6
# 2 2 5
# 1 5 2
# 2 3 5