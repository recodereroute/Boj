# maps :8 x 8
# 알파벳 : 열 , 숫자 : 행
# A : 0 ~ H : 7

king, stone, n = map(str, input().split()) # king 은 1, stone 는 -1 로 표시하자
n = int(n)
king = list(map(str, king))
stone = list(map(str, stone))

maps = [[0 for i in range(8)] for j in range(8)]

def alphaToNum(lst):
    if lst[0] == 'A': return '0'
    elif lst[0] == 'B': return '1'
    elif lst[0] == 'C': return '2'
    elif lst[0] == 'D': return '3'
    elif lst[0] == 'E': return '4'
    elif lst[0] == 'F': return '5'
    elif lst[0] == 'G': return '6'
    elif lst[0] == 'H': return '7'


def numToAlph(cha):
    if cha == 0 : return 'A'
    elif cha == 1 : return 'B'
    elif cha == 2: return 'C'
    elif cha == 3: return 'D'
    elif cha == 4: return 'E'
    elif cha == 5: return 'F'
    elif cha == 6: return 'G'
    elif cha == 7: return 'H'


def move(king, act, y, x):
    if act == 'R':
        nx = x + 1
        if 0 <= nx < 8:
            if maps[y][nx] == 0:
                    maps[y][x] = 0
                    maps[y][nx] = 1
                    king[0] = nx
            else:
                if 0 <= nx + 1 < 8:
                    maps[y][nx + 1] = -1
                    maps[y][nx] = 1
                    maps[y][x] = 0
                    king[0] = nx

    elif act == 'L':
        nx = x - 1
        if 0 <= nx < 8:
            if maps[y][nx] == 0:
                maps[y][x] = 0
                maps[y][nx] = 1
                king[0] = nx
            else:
                if 0 <= nx - 1 < 8:
                    maps[y][nx - 1] = -1
                    maps[y][nx] = 1
                    maps[y][x] = 0
                    king[0] = nx

    elif act == 'B':
        ny = y + 1
        if 0 <= ny < 8:
            if maps[ny][x] == 0:
                maps[y][x] = 0
                maps[ny][x] = 1
                king[1] = ny
            else:
                if 0 <= ny + 1 < 8:
                    maps[ny + 1][x] = -1
                    maps[ny][x] = 1
                    maps[y][x] = 0
                    king[1] = ny

    elif act == 'T':
        ny = y - 1
        if 0 <= ny < 8:
            if maps[ny][x] == 0:
                maps[y][x] = 0
                maps[ny][x] = 1
                king[1] = ny
            else:
                if 0 <= ny - 1 < 8:
                    maps[ny - 1][x] = -1
                    maps[ny][x] = 1
                    maps[y][x] = 0
                    king[1] = ny

    elif act == 'RT':
        ny = y - 1
        nx = x + 1
        if (0 <= ny < 8) and (0 <= nx < 8):
            if maps[ny][nx] == 0:
                maps[y][x] = 0
                maps[ny][nx] = 1
                king[1], king[0] = ny, nx
            else:
                if (0 <= ny - 1 < 8) and (0 <= nx + 1 < 8):
                    maps[ny - 1][nx + 1] = -1
                    maps[ny][nx] = 1
                    maps[y][x] = 0
                    king[1], king[0] = ny, nx

    elif act == 'LT':
        ny = y - 1
        nx = x - 1
        if (0 <= ny < 8) and (0 <= nx < 8):
            if maps[ny][nx] == 0:
                maps[y][x] = 0
                maps[ny][nx] = 1
                king[1], king[0] = ny, nx
            else:
                if (0 <= ny - 1 < 8) and (0 <= nx - 1 < 8):
                    maps[ny - 1][nx - 1] = -1
                    maps[ny][nx] = 1
                    maps[y][x] = 0
                    king[1], king[0] = ny, nx

    elif act == 'LB':
        ny = y + 1
        nx = x - 1
        if (0 <= ny < 8) and (0 <= nx < 8):
            if maps[ny][nx] == 0:
                maps[y][x] = 0
                maps[ny][nx] = 1
                king[1], king[0] = ny, nx
            else:
                if (0 <= ny + 1 < 8) and (0 <= nx - 1 < 8):
                    maps[ny + 1][nx - 1] = -1
                    maps[ny][nx] = 1
                    maps[y][x] = 0
                    king[1], king[0] = ny, nx

    elif act == 'RB':
        ny = y + 1
        nx = x + 1
        if (0 <= ny < 8) and (0 <= nx < 8):
            if maps[ny][nx] == 0:
                maps[y][x] = 0
                maps[ny][nx] = 1
                king[1], king[0] = ny, nx
            else:
                if (0 <= ny + 1 < 8) and (0 <= nx + 1 < 8):
                    maps[ny + 1][nx + 1] = -1
                    maps[ny][nx] = 1
                    maps[y][x] = 0
                    king[1], king[0] = ny, nx


king[0] = alphaToNum(king)
stone[0] = alphaToNum(stone)
king = list(map(int, king))
stone = list(map(int, stone))
king[1] = 8 - king[1]
stone[1] = 8 - stone[1]

maps[king[1]][king[0]] = 1 # king 은 1
maps[stone[1]][stone[0]] = -1 # stone 는 -1

for _ in range(n):
    act = input()
    x, y = king
    move(king, act, y, x)

result = ['0'] * 4
for j in range(8):
    for i in range(8):
        if maps[j][i] == 1:
            result[0], result[1] = numToAlph(i), 8 - j
        elif maps[j][i] == -1:
            result[2] , result[3] = numToAlph(i), 8 - j
print("{0}{1}".format(result[0], result[1]))
print("{0}{1}".format(result[2], result[3]))