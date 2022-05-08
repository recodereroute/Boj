# n, m, t = 노드, 간선, 목적지
# s, g, h = 시작점, g~h를 지나쳤음
# s 에서 g 까지의 최단거리 + g 에서 h 까지의 최단거리
# 위의 값이 최단 거리라면 출력 아니면 무시
# 1. 다익스트라 2. BFS -> 두가지 방식으로 다 풀릴것 같음 (다익스트라 먼저 해보고 풀리면 BFS 로 도전)
# 다익스트라 : 1) s -> g, +(g - > h) , h -> t , 2) s - > h +(h -> g), g -> t


import sys
tc = int(input())
for __ in range(tc):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    # 최단거리 리스트 - 모든 요소 무한대로 시작
    distance = [sys.maxsize] * (n+1)
    # 방문 여부 리스트
    visited = [False] * (n+1)
    # 간선정보 입력받기
    maps = [[]for i in range(n+1)]
    goals = []
    for _ in range(m):
        a, b, d = map(int, input().split())
        # 무향 그래프의 경우 양쪽 방향에 다 들어감
        maps[a].append((b, d))
        maps[b].append((a, d))
        # g_h 사이 거리
        if (a == g and b == h) or (a == h and b == g):
            g_h = d
            # print("필수코스 소요 거리 :", g_h)

    for _ in range(t):
        goals.append(int(input()))


    def smallest_cost():
        min_val = sys.maxsize
        idx = 0
        # 인덱스 값들을 0이 아닌 1부터 입력했기 때문에 (1, n+1)
        for i in range(1, n + 1):
            if distance[i] < min_val and visited[i] == False:
                min_val = distance[i]
                idx = i
        return idx


    def Dijkstra(start):
        distance[start] = 0
        visited[start] = True
        for node in maps[start]:
            distance[node[0]] = node[1]
        # 시작 노드를 제외한 n-1 번만큼 반복
        for j in range(n-1):
            now = smallest_cost()
            visited[now] = True
            # 현재 노드와 연결된 다른 노드 확인
            for i in maps[now]:
                cost = distance[now] + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost


    result = []
    tmp_t = dict()
    Dijkstra(s)
    # s -> g -> h , s -> h -> g, s->t 까지의 최소 값
    accGt = distance[g] + g_h
    # print("s-g-h : ", accGt)
    accHt = distance[h] + g_h
    # print("s-h-g", accHt)
    # t 는 값이 여러개
    for i in goals:
        tmp_t[i] = distance[i]

    for i in goals:
        # print("t까지의 최단거리 : ", tmp_t[i])
        # h -> t
        # 초기화
        distance = [sys.maxsize] * (n + 1)
        visited = [False] * (n + 1)
        Dijkstra(h)
        h_t = distance[i]
        # print("h_t", h_t)
        sGhT = accGt + h_t # S -> G -> H -> T
        # g -> t
        # 초기화
        distance = [sys.maxsize] * (n + 1)
        visited = [False] * (n + 1)
        Dijkstra(g)
        g_t = distance[i]
        # print("g_t",g_t)
        sHgT = accHt + g_t # S -> H -> G -> T
        if sHgT <= tmp_t[i] or sGhT <= tmp_t[i]:
            result.append(i)

    result.sort()
    print(*result)


#######################################################################
# g->h 로 갔다가 h->g 로 다시 돌아오는 경우를 고려 안한 틀린 풀이
        # for i in goals:
    #     # 초기화
    #     distance = [sys.maxsize] * (n + 1)
    #     visited = [False] * (n + 1)
    #     # g -> t,
    #     if g == i:
    #         g_t = 2 * g_h
    #     else:
    #         Dijkstra(g)
    #         g_t = distance[i]
    #     # 초기화
    #     distance = [sys.maxsize] * (n + 1)
    #     visited = [False] * (n + 1)
    #     # h -> t
    #     if h == i:
    #         h_t = 2 * g_h
    #     else:
    #         Dijkstra(h)
    #         h_t = distance[i]
    #     # 마지막에 tmp_t와 비교해줄거면 g_h 사이 거리도 더해줘야 함.
    #     fin_g = pre_g + g_t
    #     fin_h = pre_h + h_t
    #     # print("h경로", fin_h)
    #     # print("g경로", fin_g)
    #     # print("최소값", tmp_t[i])
    #     if fin_g <= tmp_t[i] or fin_h <= tmp_t[i]:
    #         result.append(i)
    #
    # result.sort()
    # print(*result)
# print(result)
#
#
# print(maps)
# print(goals)