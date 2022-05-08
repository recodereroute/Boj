# board = n x n
# 0 : 빈 칸 , 1 : 벽
# 출발 : (0,0) , 도착 : (n-1, n-1)
# 직선도로 : 100, 코너 : 500 - 코너를 어떻게 알아 차릴수 있는지? - 이전 진행 방향을 넣어줘야 한다.
# 최소 비용을 return 하라 -> 최단 경로 != 최소 비용

# 애매한 부분 : 방문여부를 표현하면 최단경로는 구할수 있지만 최소 비용이 아닐수 있다.
#             그렇다고 방문여부를 표현하지 않으면 너무 많은 중복된 경우들이 나온다. - 무한루프 아닌 무한루프...
# 방금 갔던곳만 못가도록 한다?(x) costMap 을 만들어서 그 칸에 들어오는 cost가 이전 cost보다 작을때만 큐에 넣어준다.
import sys
from collections import deque

board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]] # result = 3200
n = len(board)
MAXSIZE = sys.maxsize
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
result = []
def BFS():
    queue = deque()
    cnt = 0
    queue.append((0, 0, 0, 0, 0, 0)) # cnt,(0,0),dir, preY, preX 에서 시작

    costMap = [[MAXSIZE for j in range(n)] for i in range(n)]
    costMap[0][0] = 0

    while queue:
        cnt, y, x, dir, preY, preX = queue.popleft()

        if y == n-1 and x == n-1: # 목적지에 도착한 경우
            result.append(cnt)
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= n or (ny == preY and nx == preX): # 영역밖 or 방금 지나온 길
                continue

            if board[ny][nx] == 0: # 벽이 아니면서
                tmp = cnt
                if cnt == 0: # 처음 들어갈때는 무조건 직선으로 시작한다.
                    tmp += 100

                else:
                    if dir == i: # 이전 진행방향과 같은 경우
                        tmp += 100
                    else: # 코너를 도는 경우
                        tmp += 600 # 600 = 코너 : 500 + 직선 : 100

                if tmp <= costMap[ny][nx]:
                    costMap[ny][nx] = tmp
                    queue.append((tmp, ny, nx, i, y, x))
BFS()
result.sort()
print(result[0])