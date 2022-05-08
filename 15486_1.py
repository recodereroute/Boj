import sys

n = int(sys.stdin.readline())
schedule = []
for _ in range(n):
    schedule.append(list(map(int, sys.stdin.readline().split())))
dp = [0] * (n + 1)

tmp = 0
for i in range(n):
    # i 일 전까지의 최대값과 i 일이 됐을때 최대값 중 더 큰 값을 저장
    # if 문 아래로 가야하나? x -> 이번에 들어온 요소는 continue 되더라도
    # i 가 1 커지면서 tmp 에 저장 될 max 값은 바뀔 수 있다.
    tmp = max(tmp, dp[i])
    # 퇴사일을 벗어나는 경우는 고려할 필요x
    if i + schedule[i][0] > n:
        continue
    # 기존값과 새로 들어온 값 중 큰 값으로 갱신해준다.
    dp[i + schedule[i][0]] = max(dp[i + schedule[i][0]], tmp + schedule[i][1])

print(max(dp))