# 인접 : 동, 서, 남, 북, 위, 아래
# 며칠이 지나면 다 익을지 구하여라
# 익은 토마토 : 1, 안 익은 토마토 : 0, 빈 칸 : -1

from collections import deque

m, n, hei = map(int, input().split())
maps = [[]for j in range(hei)]
start = []
d = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

for k in range(hei):
    for j in range(n):
        maps[k].append(list(map(int,input().split())))
        for i in range(m):
            if maps[k][j][i] == 1:
                start.append((0, k, j, i))



def BFS():
    queue = deque(start)
    while queue:
        cnt, h, y, x = queue.popleft()
        result = cnt
        for i in range(6):
            dh, dy, dx = d[i]
            nh = h + dh
            ny = y + dy
            nx = x + dx

            if nh < 0 or ny < 0 or nx < 0 or nh >= hei or ny >= n or nx >= m:
                continue
            if maps[nh][ny][nx] == 0:
                maps[nh][ny][nx] = 1
                queue.append((cnt + 1,nh, ny, nx))

    flag = True
    for k in range(hei):
        for j in range(n):
            for i in range(m):
               if maps[k][j][i] == 0:
                   flag = False

    if flag == True:
        return cnt
    else:
        return -1

result = BFS()
print(result)
