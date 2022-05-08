# 사수가 손해를 보면 부사수도 같이 손해
# 부사수가 이득을 보면 사수도 같이 이득

from collections import deque

n, m = map(int, input().split())
lst = list(map(int, input().split()))
# 각 요소를 deque 로 만드는 이유 -> 선임은 본인보다 앞에, 후임은 뒤에 넣어서 구분해준다.
seller = [deque([i])for i in range(n+1)]
money = [0] * (n+1)

for i in range(1, len(lst)):
    # 사수는 본인 기준 앞에 추가
    seller[i+1].appendleft(lst[i])
    # 부사수는 본인 기준 뒤에 추가
    seller[lst[i]].append(i+1)
print(seller)


# 사수 찾는 함수
def find_old(num):
    for i in seller[num]:
        # 사수는 자신보다 앞에 추가했으므로 자신의 값이 나오기 전까지만 탐색
        if i == num:
            break
        operator.add(i)

    for i in operator:
        if not visited[i]:
            visited[i] = True
            find_old(i)


# 부사수 찾는 함수
def find_new(num):
    last_idx = len(seller[num]) - 1
    # 부사수는 자신보다 뒤에 추가했으므로 역순으로 탐색
    for i in range(last_idx, 0, -1):
        if seller[num][i] == num:
            break
        operator.add(seller[num][i])

    for i in operator:
        if not visited[i]:
            visited[i] = True
            find_new(i)


# 명령문들 처리
for _ in range(m):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        # 초기화
        operator = set()
        visited = [False] * (n + 1)
        idx, profit = tmp[1], tmp[2]
        # 자기자신은 방문 처리
        visited[idx] = True
        # idx 부터 last_idx 까지 반복문 돌리면서 operator 계산
        # 이득을 본 경우 - 사수들 연산
        if profit > 0:
            find_old(idx)
            operator.add(idx)
        # 손해를 본 경우 - 부사수들 연산
        else:
            find_new(idx)
            operator.add(idx)

        for i in operator:
            money[i] += profit
    else:
        print(money[idx])

print(seller)
print(money)