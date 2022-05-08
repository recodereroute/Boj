# 리스트 : 들어온 타이밍, 추천받은 횟수, 들어왔던 숫자(or 카운트)
# pic =[ [들어온 타이밍, 추천받은 횟수, 들어왔던 숫자], ["], ["] ] - 내부 값은 list or deque : 내부 추천받은 횟수는 계속해서 수정될 수 있음
# 타이밍을 맨 앞 값으로 해줘야 이걸 기준으로 sort 해줄 수 있음
# sorted 함수는 새로운 리스트값을 반환한다. -> 앞의 리스트와 이름이 같다고 얕은복사가 되는 중이 아니다.


timing = 0
pic = [[0, 0, 0] for i in range(int(input()))]# 추천수, 들어온 시간, 들어온 값
trash = int(input())
recommend = list(map(int, input().split()))

def check(inputNum , timing, pic):
    # 추천수에 대해 오름차순 정렬 후에 들어온 시간에 대해 오름차순 정렬
    pic = sorted(pic, key=lambda x: (x[0], x[1]))

    for idx, i in enumerate(pic):
        if inputNum == i[2]: # 들어온 값이 이미 리스트에 존재한다면
            pic[idx][0] += 1 # 추천횟수만 올려준다.
            return pic
    else: # 이미 추천받은 횟수, 타이밍 둘 다 오름차순으로 정렬이 되어 있으므로 맨 앞 값이 빠져야 하는 상황
        pic.pop(0)
        pic.append([1, timing, inputNum])
        return pic


for i in recommend:
    timing += 1
    pic = check(i, timing, pic)

pic = sorted(pic, key=lambda x: (x[2]))
for i in pic:
    print(i[2], end=" ")
