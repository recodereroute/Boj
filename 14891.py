# 12시방향부터 시계방향 순서대로 주어진다. N극은 0, S극은 1로 나타나있다.
# wheels[1][2], wheels[2][6]
# wheels[2][2], wheels[3][6]
# wheels[3][2], wheels[4][6]
# 결국 위의 셋을 비교하는 것
from collections import deque

wheels = [[]]
for _ in range(4):
    tmp = list(map(int , input()))
    wheels.append(tmp)
cycle = int(input())
orders = []
flags = deque()
for _ in range(cycle):
    orders.append(tuple(map(int, input().split())))

def rotate(num, dir):
    if dir == 1: # 정 방향(시계 방향)
        wheels[num][0], wheels[num][1], wheels[num][2], wheels[num][3], wheels[num][4], wheels[num][5], wheels[num][6], wheels[num][7] =\
            wheels[num][7], wheels[num][0], wheels[num][1], wheels[num][2], wheels[num][3], wheels[num][4], wheels[num][5], wheels[num][6]

    else: # 역 방향(반시계 방향)
        wheels[num][0], wheels[num][1], wheels[num][2], wheels[num][3], wheels[num][4], wheels[num][5], wheels[num][6], wheels[num][7] =\
            wheels[num][1], wheels[num][2], wheels[num][3], wheels[num][4], wheels[num][5], wheels[num][6], wheels[num][7], wheels[num][0]


for order in orders:
    num, dir = order[0], order[1]
    if num == 1:
        if wheels[1][2] != wheels[2][6]:
            flags.append((2, -dir))
            if wheels[2][2] != wheels[3][6]:
                flags.append((3, dir))
                if wheels[3][2] != wheels[4][6]:
                    flags.append((4, -dir))
    elif num == 2:
        if wheels[2][6] != wheels[1][2]:
            flags.append((1, -dir))
        if wheels[2][2] != wheels[3][6]:
            flags.append((3, -dir))
            if wheels[3][2] != wheels[4][6]:
                flags.append((4, dir))
    elif num == 3:
        if wheels[3][2] != wheels[4][6]:
            flags.append((4, -dir))
        if wheels[3][6] != wheels[2][2]:
            flags.append((2, -dir))
            if wheels[2][6] != wheels[1][2]:
                flags.append((1, dir))
    elif num == 4:
        if wheels[4][6] != wheels[3][2]:
            flags.append((3, -dir))
            if wheels[3][6] != wheels[2][2]:
                flags.append((2, dir))
                if wheels[2][6] != wheels[1][2]:
                    flags.append((1, -dir))
    rotate(num, dir)
    for _ in range(len(flags)):
        num, dir = flags.popleft()
        rotate(num, dir)


result = 0
if wheels[1][0] == 1:
    result += 1
if wheels[2][0] == 1:
    result += 2
if wheels[3][0] == 1:
    result += 4
if wheels[4][0] == 1:
    result += 8

print(result)