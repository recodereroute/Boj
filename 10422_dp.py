tc = int(input())

lst = []
dy = [0] * 5001
# 간단하게 구할 수 있는 초기값은 주고 시작
dy[0], dy[2], dy[4] = 1, 1, 2

for _ in range(tc):
    l = int(input())
    lst.append(l)
    # 가장 큰 값에 대한 DP 를 한번만 계산하고 그보다 작은 값은 이전 계산 값으로 출력한다.
    chance = max(lst)

for num in range(6, chance + 1, 2):
    for i in range(2, num + 1, 2):
        dy[num] += dy[i-2] * dy[num - i]
for i in lst:
    print(dy[i] % 1000000007)

