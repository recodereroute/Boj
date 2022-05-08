import copy

cube = dict()
for i in range(1, 25):
    cube[i] = i

lst = list(map(int, input().split()))
for idx, i in enumerate(lst):
    cube[idx+1] = i


def confirm(maps):
    for j in range(6):
        cnt = []
        # 각 면마다 구성하는 색을 확인
        for i in range(j*4+1, j*4+5):
            cnt.append(maps[i])
        cnt.sort()
        # 색이 하나라도 다를경우 무조건 False
        if cnt[0] != cnt[3]:
            return False
            break
    return True


# 연산용 딕셔너리
tmp = copy.deepcopy(cube)
# 윗면 오른쪽 회전
tmp[13], tmp[14], tmp[5], tmp[6], tmp[17], tmp[18], tmp[21], tmp[22], tmp[1], tmp[2], tmp[3], tmp[4] =\
    tmp[21], tmp[22], tmp[13], tmp[14], tmp[5], tmp[6], tmp[17], tmp[18], tmp[2], tmp[4], tmp[1], tmp[3]
flag = confirm(tmp)
if flag is True:
    print(1)
    exit(0)
# 초기화
tmp = copy.deepcopy(cube)
# 윗면 왼쪽 회전
tmp[13], tmp[14], tmp[5], tmp[6], tmp[17], tmp[18], tmp[21], tmp[22], tmp[1], tmp[2], tmp[3], tmp[4] =\
    tmp[5], tmp[6], tmp[17], tmp[18], tmp[21], tmp[22], tmp[13], tmp[14], tmp[3], tmp[1], tmp[4], tmp[2]
flag = confirm(tmp)
if flag is True:
    print(1)
    exit(0)
# 초기화
tmp = copy.deepcopy(cube)
# 아랫면 오른쪽 회전
tmp[15], tmp[16], tmp[7], tmp[8], tmp[19], tmp[20], tmp[23], tmp[24], tmp[9], tmp[10], tmp[11], tmp[12] =\
    tmp[23], tmp[24],tmp[15], tmp[16], tmp[7], tmp[8], tmp[19], tmp[20], tmp[11], tmp[9], tmp[12], tmp[10]
flag = confirm(tmp)
if flag is True:
    print(1)
    exit(0)
# 초기화
tmp = copy.deepcopy(cube)
# 아랫면 왼쪽 회전
tmp[15], tmp[16], tmp[7], tmp[8], tmp[19], tmp[20], tmp[23], tmp[24], tmp[9], tmp[10], tmp[11], tmp[12] = \
    tmp[7], tmp[8], tmp[19], tmp[20], tmp[23], tmp[24],tmp[15], tmp[16], tmp[10], tmp[12], tmp[9], tmp[11]
flag = confirm(tmp)
if flag is True:
    print(1)
    exit(0)
# 초기화
tmp = copy.deepcopy(cube)
# 오른쪽면 위로 회전 -> 테스트 케이스 확인 가능o
tmp[2], tmp[4], tmp[6], tmp[8], tmp[10], tmp[12], tmp[21], tmp[23], tmp[17], tmp[18], tmp[19], tmp[20] =\
    tmp[6], tmp[8], tmp[10], tmp[12], tmp[23], tmp[21], tmp[4], tmp[2], tmp[19], tmp[17], tmp[20], tmp[18]
flag = confirm(tmp)
if flag is True:
    print(1)
    exit(0)
# 초기화
tmp = copy.deepcopy(cube)
# 오른쪽면 아래로 회전
tmp[2], tmp[4], tmp[6], tmp[8], tmp[10], tmp[12], tmp[21], tmp[23], tmp[17], tmp[18], tmp[19], tmp[20] =\
    tmp[23], tmp[21], tmp[2], tmp[4], tmp[6], tmp[8], tmp[12], tmp[10], tmp[18], tmp[20], tmp[17], tmp[19]
flag = confirm(tmp)
if flag is True:
    print(1)
    exit(0)
# 초기화
tmp = copy.deepcopy(cube)
# 왼쪽면 위로 회전
tmp[1], tmp[3], tmp[5], tmp[7], tmp[9], tmp[11], tmp[22], tmp[24], tmp[13], tmp[14], tmp[16], tmp[15] =\
    tmp[5], tmp[7], tmp[9], tmp[11], tmp[24], tmp[22], tmp[3], tmp[1], tmp[14], tmp[16], tmp[15], tmp[13]
flag = confirm(tmp)
if flag is True:
    print(1)
    exit(0)
# 초기화
tmp = copy.deepcopy(cube)
# 왼쪽면 아래로 회전
tmp[1], tmp[3], tmp[5], tmp[7], tmp[9], tmp[11], tmp[22], tmp[24], tmp[13], tmp[14], tmp[16], tmp[15] =\
   tmp[24], tmp[22], tmp[1], tmp[3], tmp[5], tmp[7],tmp[11], tmp[9], tmp[15], tmp[13], tmp[14], tmp[16]
flag = confirm(tmp)
if flag is True:
    print(1)
    exit(0)
# 초기화
tmp = copy.deepcopy(cube)
# 센터 윗면 오른쪽 회전
tmp[5], tmp[6], tmp[7], tmp[8], tmp[3], tmp[4], tmp[17], tmp[19], tmp[9], tmp[10], tmp[14], tmp[16] =\
    tmp[7], tmp[5], tmp[8], tmp[6], tmp[16], tmp[14], tmp[3], tmp[4], tmp[19], tmp[17], tmp[9], tmp[10]
flag = confirm(tmp)
if flag is True:
    print(1)
    exit(0)
# 초기화
tmp = copy.deepcopy(cube)
# 센터 윗면 왼쪽 회전
tmp[5], tmp[6], tmp[7], tmp[8], tmp[3], tmp[4], tmp[17], tmp[19], tmp[9], tmp[10], tmp[14], tmp[16] =\
    tmp[6], tmp[8], tmp[5], tmp[7], tmp[17], tmp[19], tmp[10], tmp[9], tmp[14], tmp[16], tmp[4], tmp[3]
flag = confirm(tmp)
if flag is True:
    print(1)
    exit(0)
# 초기화
tmp = copy.deepcopy(cube)
# 센터 아래면 오른쪽 회전
tmp[21], tmp[22], tmp[23], tmp[24], tmp[4], tmp[3], tmp[14], tmp[16], tmp[11], tmp[12], tmp[20], tmp[18] =\
    tmp[23], tmp[21], tmp[24], tmp[22], tmp[20], tmp[18], tmp[4], tmp[3], tmp[14], tmp[16], tmp[11], tmp[12]
flag = confirm(tmp)
if flag is True:
    print(1)
    exit(0)
# 초기화
tmp = copy.deepcopy(cube)
# 센터 아래면 왼쪽 회전
tmp[21], tmp[22], tmp[23], tmp[24], tmp[4], tmp[3], tmp[14], tmp[16], tmp[11], tmp[12], tmp[20], tmp[18] =\
   tmp[22], tmp[24], tmp[21], tmp[23], tmp[14], tmp[16], tmp[11], tmp[12], tmp[20], tmp[18], tmp[4], tmp[3]
flag = confirm(tmp)
if flag is True:
    print(1)
    exit(0)

if flag is not True:
    print(0)