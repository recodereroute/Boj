# 인접 : 상,하,좌,우
# 1. 비어있는 칸 중 좋아하는 학생이 가장 많이 인접한 칸
# 2. 1을 만족하는 칸이 여러개면 가장 인접한 빈자리가 많은경우
# 3. 2를 만족하는 칸이 여러개면 행이 가장 작은 칸 -> 열이 가장 작은 칸
# 만족도 : 0 - 0 , 1 - 1, 2 - 10, 3 - 100, 4 - 1000
import copy
from collections import deque

n = int(input())

maps = [[0 for j in range(n)] for i in range(n)] # 배치용
matrix = [[0 for j in range(n)] for i in range(n)] # 연산용
satFav = [[] for i in range(n*n)]
favorite = deque()
start = deque()

for i in range(n*n):
    s, w1, w2, w3, w4 = map(int, input().split())
    start.append(s-1) # 시작할 요소와
    favorite.append([w1-1, w2-1, w3-1, w4-1]) # 원하는 요소를 각각 리스트로 만듬
    satFav[s-1] = [w1, w2, w3, w4]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

s1 = start.popleft() # 첫 요소는 1,1 고정
maps[1][1] = s1 + 1 # 요소들 전부 인덱스 값으로 받아오느라 1씩 빼줬으니 보상
favorite.popleft() # 첫 요소 관련 내용 제거 (이 부분을 안해줬던거 같음...)

def move():
    # 1번 조건
    while start: # 빼줘야할 전부가 끝난경우
        s = start.popleft()
        w1, w2, w3, w4 = favorite.popleft()

        tmp = copy.deepcopy(matrix) # 연산용
        tmpCan = set()
        for j in range(n):
            for i in range(n):
                if maps[j][i] == w1 + 1 or maps[j][i] == w2 + 1 or maps[j][i] == w3 + 1 or maps[j][i] == w4 + 1: # 원하는 값이 발견되면
                    for k in range(4):
                        ny = j + dy[k]
                        nx = i + dx[k]
                        if ny < 0 or nx < 0 or ny >= n or nx >= n: # 맵을 벗어나면
                            continue
                        if maps[ny][nx] == 0: # 빈자리인 경우
                            tmp[ny][nx] += 1 # 가장 카운팅 많이 된곳에 앉혀줄거임.
                            tmpCan.add((ny, nx)) # 앉혀질 가능성이 있는 자리들
        cnt = 1
        cntCan = []
        for obj in tmpCan:
            y, x = obj
            if tmp[y][x] > cnt: # 더 큰 카운팅 값이 들어오면
                cnt = tmp[y][x] # 그 값 저장
                cntCan.clear() # 이전까지 받은값 제거
                cntCan.append((y, x)) # 방금 받은값 저장
            elif tmp[y][x] == cnt: # 같은 카운팅 값이 여러개라면
                cntCan.append((y,x)) # 두번째 조건을 실행해 줄 지표가 됨 - cntCan에 가능성 있는 것들이 저장되고 있음

        if len(cntCan) == 1: # 많이 카운팅 된게 유일한경우
            y, x = cntCan[0]
            maps[y][x] = s + 1 # 그 자리를 채워준다.
            continue

        # 2번 조건 (여기서 헷갈림 - '1을 만족하는 칸이 여러개' 라고 했는데, 하나도 만족하지 않는 경우도 2로 넘어옴)
        if len(cntCan) == 0: # 1을 하나도 만족 못한 경우
            for j in range(n):
                for i in range(n): # tmp 에 카운팅 된곳이 하나도 없을테니 새로 카피 안해줘도 됨.
                    if maps[j][i] == 0: # 빈칸인 경우 4방향 카운팅 - 가장많이 카운팅 된 곳에 앉혀줄거임
                        for k in range(4):
                            ny = j + dy[k]
                            nx = i + dx[k]
                            if ny < 0 or nx < 0 or ny >= n or nx >= n:  # 맵을 벗어나면
                                continue
                            if maps[ny][nx] == 0:  # 빈자리인 경우
                                tmp[ny][nx] += 1  # 가장 카운팅 많이 된곳에 앉혀줄거임.
                                tmpCan.add((ny, nx))  # 앉혀질 가능성이 있는 자리들
            cnt = 0 # 인접한 자리와는 다르게 주변 빈자리는 한칸도 존재하지 않는 경우도 있다.
                    # 한칸도 존재하지 않는경우에도 cntCan 의 길이를 늘려서 조건 3으로 보내줘야 하므로 cnt는 0부터 시작.
            for obj in tmpCan:
                y, x = obj
                if tmp[y][x] > cnt:
                    cnt = tmp[y][x]
                    cntCan.clear()
                    cntCan.append((y, x))
                elif tmp[y][x] == cnt:
                    cntCan.append((y, x))

            if len(cntCan) == 1:
                y, x = cntCan[0]
                maps[y][x] = s + 1
                continue # 채워 줬으면 다음 차례 진행

        elif len(cntCan) > 0 : # 1 조건을 만족하는게 여러개인 경우
            tmp = copy.deepcopy(matrix) # 카운팅 된것들 초기화
            tmpCan.clear() # tmpCan에는 적게 카운팅 된 자리들도 남아있음 - 전부 지워주기.

            # for obj in tmpCan: # 많이 카운팅 된곳들(cntCan) 기준으로 4방향을 찾아본다. - tmpCan 아님.
            for obj in cntCan:
                y, x = obj
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if ny < 0 or nx < 0 or ny >= n or nx >= n:  # 맵을 벗어나면
                        continue
                    if maps[ny][nx] == 0:
                        tmp[y][x] += 1 # 주변에 빈자리가 발견되면 자기 자신에 카운팅을 해준다.
                        tmpCan.add((y, x)) # 주변에 빈자리가 발견된 자리

            if len(tmpCan) == 0: # 만약 한칸도 빈자리가 없었다면 이전에 있던 값들 그대로 들고온다.
                tmpCan = set(cntCan) # 이거 안해주면 조건3에서 len(cntCan) == 0 으로 진입해 버림. -> 여기서 틀렸음.
            cntCan.clear()
            cnt = 0 # 인접한 자리와는 다르다. - 채워주는 후반부로 갈수록 빈자리가 없는 경우가 발생할 수 있다.
            for obj in tmpCan:
                y, x = obj
                if tmp[y][x] > cnt:
                    cnt = tmp[y][x]
                    cntCan.clear()
                    cntCan.append((y, x))
                elif tmp[y][x] == cnt:
                    cntCan.append((y, x))


            if len(cntCan) == 1:
                y, x = cntCan[0]
                maps[y][x] = s + 1
                continue  # 채워 줬으면 다음 차례 진행

        # 3번 조건
        if len(cntCan) == 0: # 하나도 만족 못해서 3번까지 온 경우
            flag = True
            for j in range(n):
                for i in range(n):
                    if maps[j][i] == 0: # 가장 먼저 찾아지는 빈자리에 앉혀줌
                        maps[j][i] = s+1
                        flag = False
                        break
                if flag == False:
                    break
            continue
        elif len(cntCan) > 1: # 만족하는게 여러개여서 넘어온 경우
            # tmpCan이 아니라 cntCan을 sort 해줘야 한다. - tmpCan에서 많이 카운팅돼서 넘어온게 cntCan
            cntCan.sort()
            y, x = cntCan[0]
            maps[y][x] = s + 1 # 오름차순 정렬된 가장 첫번째 값에 앉혀줌

def satisfy(maps):
    result = 0
    for j in range(n):
        for i in range(n):
            cnt = 0
            idx = maps[j][i] - 1# 인덱스 넘버
            w1, w2, w3, w4 = satFav[idx]
            for k in range(4):
                ny = j + dy[k]
                nx = i + dx[k]

                if ny < 0 or nx < 0 or ny >= n or nx >= n:
                    continue
                if maps[ny][nx] == w1 or maps[ny][nx] == w2 or maps[ny][nx] == w3 or maps[ny][nx] == w4:
                    cnt += 1

            if cnt == 1:
                result += 1
            elif cnt == 2:
                result += 10
            elif cnt == 3:
                result += 100
            elif cnt == 4:
                result += 1000
    return result


move()
result = satisfy(maps)
print(result)