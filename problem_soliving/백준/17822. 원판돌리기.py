import sys

sys.stdin = open('input', 'r')


# 탐색
def bfs(i, j):
    global zero
    q = [[i, j]]
    visited[i][j] = 1
    while q:
        x, y = q.pop(0)
        # 지워진 수가 있나 없나 확인하기 위해
        # zero_cnt = 0
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni = x + di
            nj = y + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if circle[x][y] == circle[ni][nj]:
                    circle[x][y] = circle[ni][nj] = 0
                    visited[ni][nj] = 1
                    zero += 1
                # else:
                #     if circle[ni][nj] != 0:
                #         q.append([ni, nj])
    return circle


# 회전하는 함수 만들기
def move(arr, d, t):
    if d == 0:
        for x in range(t):
            pick = arr.pop()
            arr.insert(0, pick)
        return arr
    else:
        for x in range(t):
            pick = arr.pop(0)
            arr.append(pick)
        return arr


# 반지름크기, 원판의 개수, 회전 수
N, M, T = map(int, input().split())
circle = [list(map(int, input().split())) for x in range(M)]
# x의 배수원판을, d방향으로(0은 시계, 1 반시계), t번 돌린다
info = [list(map(int, input().split())) for x in range(T)]
visited = [[0] * M for x in range(N)]
zero = 0
# 정보를 정리하기
for a in range(T):
    x, d, t = info[a]
    multiple = []
    # 배수인 원판을 찾아서 돌려야함
    for b in range(M):
        if (b + 1) % x == 0:
            multiple.append(b)
    # 원판을 돌려보기
    for s in range(len(multiple)):
        modify = move(circle[multiple[s]], d, t)
        circle[multiple[s]] = modify
    # 탐색하면서 주변에 같은 수 있으면 지우기
    # 아니면 다른 처리하기
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                circle = bfs(i, j)
print(circle)
# 지워진 숫자가 있냐 없냐고 판단해서 합구하기
ans = 0
if zero != 0:
    for i in range(N):
        for j in range(M):
            ans += circle[i][j]
else:
    # 평균을 구하기
    total = 0
    cnt = 0
    for i in range(N):
        for j in range(M):
            total += circle[i][j]
            cnt += 1
    avg = total / cnt

    # 평균보다 큰 값 작은 값 정리
    for i in range(N):
        for j in range(M):
            if circle[i][j] > avg:
                circle[i][j] -= 1
            elif circle[i][j] < avg:
                circle[i][j] += 1

    # 합계 구하기
    for x in range(N):
        for y in range(M):
            ans += circle[x][y]
print(ans)






