import sys

sys.stdin = open('input.txt', 'r')


# 몇번 자석인지, 방향
def move(n, d):
    check = magnetic[n]
    # 시계 방향으로
    if d == 1:
        for x in range(1):
            check.insert(0, 0)
            check[0] = check[-1]
            check.pop()

    # 반시계방향으로
    else:
        for x in range(1):
            check.append(0)
            check[-1] = check[0]
            check.pop(0)
    return

# 각 자석별로 체크할 인덱스를 정리하기
di = [[0, 2, 0, 0], [6, 0, 2, 0], [0, 6, 0, 2], [0, 0, 6, 0]]


# 돌아갈 수 있는 것이 무엇인가
# 자석 번호랑 방향
def check(n, d):
    stack = []
    # 연결을 확인하면 체크하기
    visited = [0] * 4
    # 자석 번호를 넣기
    stack.append(n)
    # 나중에 visited를 이용해서 돌리기 위해
    visited[n] = d
    while stack:
        num = stack.pop()
        for i in range(len(di[num])):
            # 해당 자석의 연결부분
            near = di[num][i]
            if near != 0 and visited[i] == 0:
                # 다음 자석과 지금 자석의 연결부분
                next = di[i][num]
                if magnetic[num][near] != magnetic[i][next]:
                    stack.append(i)
                    # 연결되어 있으면 반대로 돌아야함
                    visited[i] = -visited[num]
    for i in range(len(visited)):
        # visited에 방향을 표시
        if visited[i] != 0:
            dir_ = visited[i]
            move(i, dir_)


T = int(input())
for tc in range(1, T + 1):
    # 자석을 돌릴 횟수
    N = int(input())
    magnetic = [list(map(int, input().split())) for x in range(4)]
    infos = []
    for i in range(N):
        n, d = list(map(int, input().split()))
        infos.append([n - 1, d])

    for j in range(N):
        num, direction = infos.pop(0)
        check(num, direction)
    # 점수 정리
    score = [1, 2, 4, 8]
    total = 0
    for i in range(4):
        if magnetic[i][0] == 1:
            total += score[i]
    print('#{} {}'.format(tc, total))