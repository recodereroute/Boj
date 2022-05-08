from collections import deque
n, m, y, x, k = map(int, input().split())
dice=[0] * 7
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))
requests = deque(map(int, input().split()))

dir = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)] # 동 서 남 북

def move(idx):
    if idx == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif idx == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif idx == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif idx == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]

while requests:
    idx = requests.popleft()
    dy, dx = dir[idx]
    ny = y + dy
    nx = x + dx

    if ny < 0 or nx < 0 or ny >= n or nx >= m:
        continue

    move(idx)
    if maps[ny][nx] == 0:
        maps[ny][nx] = dice[1]
    else:
        dice[1] = maps[ny][nx]
        maps[ny][nx] = 0

    y, x = ny, nx
    print(dice[6])