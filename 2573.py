# maps = n x m
# 빙산은 양수, 바다는 0으로 표현
# 빙산의 양은 동,서,남,북 방향 중 바다와 맞닿아 있는 칸 만큼 줄어듬 - 0보다 작아지지 않음
# 동,서,남,북으로 맞닿아 있는 빙산들은 한 덩어리로 본다
# 이 빙산(최초에 한 덩어리만 주어짐)이 최초로 두 덩어리 이상으로 나뉘는데 걸리는 시간을 구하라(다 녹을때까지 나뉘어지지 않으면 0을 출력)
from collections import deque

n, m = map(int, input().split())
years = 0
maps = []
ice = []
for j in range(n):
    tmp = list(map(int, input().split()))
    maps.append(tmp)
    for i, val in enumerate(tmp):
        if val != 0:
            ice.append((j, i))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def check_slice(ice):
    cnt = 1
    queue = deque()
    visit = [[False for i in range(m)] for j in range(n)]
    if len(ice) == 0 or len(ice) == 1:
        return 0
    y, x = ice[0]
    queue.append((y, x))
    visit[y][x] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if maps[ny][nx] != 0 and visit[ny][nx] is False:
                queue.append((ny, nx))
                visit[ny][nx] = True
                cnt += 1
    if cnt == len(ice):
        return 2
    else:
        return 1


def melting(ice, maps):
    calcul = [[0 for i in range(m)] for j in range(n)]
    for y, x in ice:
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if maps[ny][nx] == 0:
                calcul[y][x] -= 1
    for j in range(1, n-1):
        for i in range(1, m-1):
            maps[j][i] += calcul[j][i]
            if calcul[j][i] != 0 and maps[j][i] <= 0:
                ice.remove((j, i))
                maps[j][i] = 0


while True:
    years += 1
    melting(ice, maps)
    result = check_slice(ice)
    if result == 0:
        print(0)
        break
    elif result == 1:
        print(years)
        break