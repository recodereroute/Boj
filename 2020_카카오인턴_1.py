# 1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
# 2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
# 3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
# 4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
# 4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

# 순서대로 누를 번호가 담긴 배열 : numbers, 왼손잡이인지 오른손 잡이인지 담긴 hand = "left" or "right"
from collections import deque
import copy

numbers = [0,0]
hand = "right"
result = []
maps =[[0 for j in range(3)] for i in range(4)]
l = (3, 0)
r = (3, 2)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def find(y, x, hand):
    cnt = 0
    tmp = copy.deepcopy(maps)
    start = deque()
    hy, hx = hand
    if hy == y and hx == x: # 현재위치와 목표가 같은 위치라면
        return 0
    tmp[hy][hx] = 1
    start.append((cnt, hy, hx))
    tmp[y][x] = -1 # 목표지점 : -1

    while start:
        cnt, y, x = start.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny > 3 or nx > 2:
                continue
            if tmp[ny][nx] == -1:
                return cnt + 1
            elif tmp[ny][nx] == 0:
                tmp[ny][nx] = 1
                start.append((cnt + 1, ny, nx))


for num in numbers:
    # case : 왼손
    if num == 1:
        result.append("L")
        l = (0, 0)
        continue
    elif num == 4:
        result.append("L")
        l = (1, 0)
        continue
    elif num == 7:
        result.append("L")
        l = (2, 0)
        continue

    # case : 오른손
    elif num == 3:
        result.append("R")
        r = (0, 2)
        continue
    elif num == 6:
        result.append("R")
        r = (1, 2)
        continue
    elif num == 9:
        result.append("R")
        r = (2, 2)
        continue

    # case : 중앙
    elif num == 2:
        l_cnt = find(0, 1, l)
        r_cnt = find(0, 1, r)
        if l_cnt > r_cnt:
            result.append("R")
            r = (0, 1)
            continue
        elif l_cnt < r_cnt:
            result.append("L")
            l = (0, 1)
            continue
        else:
            if hand == "right":
                result.append("R")
                r = (0, 1)
                continue
            else:
                result.append("L")
                l = (0, 1)
                continue
    elif num == 5:
        l_cnt = find(1, 1, l)
        r_cnt = find(1, 1, r)
        if l_cnt > r_cnt:
            result.append("R")
            r = (1, 1)
            continue
        elif l_cnt < r_cnt:
            result.append("L")
            l = (1, 1)
            continue
        else:
            if hand == "right":
                result.append("R")
                r = (1, 1)
                continue
            else:
                result.append("L")
                l = (1, 1)
                continue
    elif num == 8:
        l_cnt = find(2, 1, l)
        r_cnt = find(2, 1, r)
        if l_cnt > r_cnt:
            result.append("R")
            r = (2, 1)
            continue
        elif l_cnt < r_cnt:
            result.append("L")
            l = (2, 1)
            continue
        else:
            if hand == "right":
                result.append("R")
                r = (2, 1)
                continue
            else:
                result.append("L")
                l = (2, 1)
                continue
    elif num == 0:
        l_cnt = find(3, 1, l)
        r_cnt = find(3, 1, r)
        if l_cnt > r_cnt:
            result.append("R")
            r = (3, 1)
            continue
        elif l_cnt < r_cnt:
            result.append("L")
            l = (3, 1)
            continue
        else:
            if hand == "right":
                result.append("R")
                r = (3, 1)
                continue
            else:
                result.append("L")
                l = (3, 1)
                continue
answer = ""
for i in result:
    answer += i
print(answer)