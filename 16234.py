# maps = n x n
# l 이상 r 이하인 경계는 open
# open 된 나라들은 똑같이 분배, 소수점 이하는 절삭


import copy
from collections import deque

n, l, r = map(int, input().split())
maps = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
check = [[False for j in range(n)] for i in range(n)]
for j in range(n):
    maps.append(list(map(int, input().split())))


def BFS(y, x):
    queue = deque()
    queue.append((y, x))
    tmp = deque()
    val, cnt = 0, 0
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            # 합이 범위안에 들어오고 이미 조사한 영역이 아니라면
            if l <= abs(maps[y][x] - maps[ny][nx]) <= r and check[ny][nx] == False:
                queue.append((ny, nx))
                tmp.append((ny, nx))
                val += maps[ny][nx]
                cnt += 1
                check[ny][nx] = True

    if cnt != 0:
        val = val // cnt
        for obj in tmp:
            y, x = obj[0], obj[1]
            maps[y][x] = val

day = 0
while True:
    tmpMaps = copy.deepcopy(maps)
    for j in range(n):
        for i in range(n):
            if check[j][i] == False:
                BFS(j, i)

    if maps == tmpMaps:
        break
    else:
        day += 1
        check = [[False for j in range(n)] for i in range(n)] # 초기화

print(day)