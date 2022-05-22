# 출발은 상근이네 집에서 하고, 맥주 한 박스를 들고 출발한다. 맥주 한 박스에는 맥주가 20개 들어있다.
# 목이 마르면 안되기 때문에 50미터에 한 병씩 마시려고 한다. - 기본값 : 20 x 50 = 1000
# 즉, 50미터를 가려면 그 직전에 맥주 한 병을 마셔야 한다.
# 편의점에 들렸을 때, 빈 병은 버리고 새 맥주 병을 살 수 있다 - 하지만 박스에 들어있는 맥주는 20개를 넘을 수 없다.
# 편의점을 나선 직후에도 50미터를 가기 전에 맥주 한 병을 마셔야 한다.
# case1) 도착점 - 출발점 <= 1000 -> happy
# case2) 도착점 - 출발점 > 1000
# -> 출발점에서 모든 편의점 까지 거리 탐색 -> 해당 편의점 - 도착점 <= 1000 -> happy
# 해당 편의점 - 도착점 > 1000 이면 편의점 기준 다른 모든 편의점 탐색 후 도착점과 거리 비교 -> 중간에 하나라도 발견되면 happy, 하나도 없는경우 sad 리턴
# 각 케이스마다 true, false 구분해줄 flag 필요할듯
from collections import deque

tc = int(input())
result_set = []
for _ in range(tc):
    result_flag = False
    n = int(input())
    visited = [True]*n
    start_x, start_y = map(int, input().split())
    store = deque()
    for __ in range(n):
        tmp_x, tmp_y = map(int, input().split())
        store.append((tmp_x, tmp_y))
    end_x, end_y = map(int, input().split())

    # case 1)
    if abs(start_x - end_x) + abs(start_y - end_y) <= 1000:
        result_set.append("happy")
        result_flag = True
    # case 2)
    else:
        queue = deque()
        queue.append((start_x, start_y))
        while(queue):
            # 현재 위치에서 모든 편의점 조회하면서 1000m 안에있는 것들만 queue에 넣어준다.
            x, y = queue.popleft()
            # 현재 위치에서 페스티벌까지 한번에 갈수있는지 조회
            if abs(x - end_x) + abs(y - end_y) <= 1000:
                result_set.append("happy")
                result_flag = True
                break
            for i in range(n):
                nx, ny = store[i]
                if visited[i] is True and abs(x - nx) + abs(y - ny) <= 1000:
                    queue.append((nx, ny))
                    visited[i] = False

        if result_flag is False:
            result_set.append("sad")

for result in result_set:
    print(result)