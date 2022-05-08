# maps : R x C
# X : 땅, . : 바다
# 인접한 3칸 또는 4칸이 바다인 땅은 시간경과후 바다로 변한다.
# 섬의 개수가 오늘날보다 적어질 것이기 때문에, 지도의 크기도 작아져야 한다. 지도의 크기는 모든 섬을 포함하는 가장 작은 직사각형이다.
# 50년이 지난 후에도 섬은 적어도 한 개 있다. 또, 지도에 없는 곳, 지도의 범위를 벗어나는 칸은 모두 바다이다.
# BFS 도 필요없이 '스타트' 기준으로 4방향 탐색만 해주면 될듯

r, c = map(int, input().split())

maps = [[] for _ in range(r)]
start = []
convert = []
for j in range(r):
    tmp = list(map(str, input().split()))
    for i in range(c):
        maps[j].append(tmp[0][i])
        if tmp[0][i] == 'X':
            start.append((j, i))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def Sink(maps, y, x):
    cnt = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= r or nx >= c:
            cnt += 1 # 영역 밖은 바다로 취급
            continue
        if maps[ny][nx] == '.':
            cnt += 1
    if cnt >= 3:
        convert.append((y, x))

for onStart in start:
    Sink(maps,onStart[0], onStart[1])

for obj in convert:
    y, x = obj[0], obj[1]
    maps[y][x] = '.'
    start.remove((y,x))

minR, minC = start[0]
maxR, maxC = start[0]

for obj in start:
    y, x = obj[0], obj[1]
    if y < minR:
        minR = y
    elif y > maxR:
        maxR = y
    if x < minC:
        minC = x
    elif x > maxC:
        maxC = x

for j in range(minR, maxR + 1):
    result = ''
    for i in range(minC, maxC + 1):
        result += maps[j][i]
        # print(*maps[j][i], end='')
    print(result)