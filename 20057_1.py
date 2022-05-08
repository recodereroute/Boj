# maps = n x n
# A[r][c] = 모래의 양
# 토네이도 A[n/2][n/2] 에서 시작 : 서, 남, 동, 북 순으로 진행 , 토네이도 시작 포인트에는 모래가 없음
# 두 번 진행할때마다 움직여야될 거리가 1씩 증가 - EX) 서,남 : 1 칸 -> 북,동 : 2칸 -> 서,남 : 3칸

import sys

n = int(sys.stdin.readline())
sand = []
tonado_start = int((n - 1) / 2)
tonado = [(tonado_start, tonado_start)]

for _ in range(n):
    sand.append(list(map(int, sys.stdin.readline().split())))

move = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 서 남 동 북
result = 0

left = [[0,-2,0.05],[1,-1,0.1],[-1,-1,0.1],[1,0,0.07],[-1,0,0.07],[2,0,0.02],[-2,0,0.02],[1,1,0.01],[-1,1,0.01]]
right = [[0,2,0.05],[1,1,0.1],[-1,1,0.1],[1,0,0.07],[-1,0,0.07],[2,0,0.02],[-2,0,0.02], [1,-1,0.01],[-1,-1,0.01]]
up = [[-2,0,0.05], [-1,1,0.1], [-1,-1,0.1], [0,1,0.07],[0,2,0.02], [0,-1,0.07],[0,-2,0.02], [1,1,0.01],[1,-1,0.01]]
down = [[2,0,0.05], [1,1,0.1], [1,-1,0.1], [0,1,0.07],[0,2,0.02], [0,-1,0.07],[0,-2,0.02], [-1,1,0.01],[-1,-1,0.01]]
moveList =[left, down, right, up] # 서 , 남 , 동, 북
result = 0


def move_tonado(flag):
    y, x = tonado.pop()
    dy, dx = move[flag]
    ny, nx = y + dy, x + dx
    if ny < 0 or nx < 0 or ny >= n or nx >= n:
        pass
    else:
        tonado.append((ny, nx))

def cal2(flag): # flag == 방향을 의미 -> 0~3 : 서 남 동 북
    result = 0
    cal = moveList[flag]
    dy,dx = move[flag]
    ty, tx = tonado[0]
    initSand = sand[ty][tx] # 모래 초기 값

    tmp = []
    for obj in cal:
        tmp.append(int(obj[2] * initSand))
        ny = ty + obj[0]
        nx = tx + obj[1]
        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            result += int(obj[2] * initSand)
        else:
            sand[ny][nx] += int(obj[2] * initSand)

    initSand -= sum(tmp)
    alpha = [ty + dy, tx + dx, initSand]
    if alpha[0] < 0 or alpha[1] < 0 or alpha[0] >= n or alpha[1] >= n:
        result += int(alpha[2])
    else:
        sand[alpha[0]][alpha[1]] += int(alpha[2])

    return result


cnt = 0
for j in range(1, sys.maxsize):
    tmp = 0
    for i in range(2 * j):
        tmp += 1
        move_tonado(cnt)
        if len(tonado) == 0: # 토네이도 소멸된 상태라면
            break
        result += cal2(cnt)
        if tmp == j:
            cnt = (cnt + 1) % 4  # 0 ~ 3까지만 출력되게 하기 위해서

    if len(tonado) == 0:
        break
    cnt = (cnt + 1) % 4

print(result)