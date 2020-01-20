import sys
sys.stdin = open('input', 'r')

# 회전(회전시킬것, 방향, 횟수)
def move(list, d, t):
    # 시계방향
    if d ==0:
        for x in range(t):
            pick = list.pop()
            list.insert(0, pick)
    else:
        for x in range(t):
            pick = list.pop(0)
            list.append(pick)

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
# 탐색
def bfs(i, j):
    visited[i][j] = 1
    q = [[i, j]]
    # 지워지는 숫자를 체크
    zero = 0
    first = board[i][j]
    while q:
        x, y = q.pop(0)
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            # 원판이기때문에 마지막과 처음이 같음
            if 0<=ni<N and -M<=nj<=M :
                if nj ==M:
                    nj =0
                # 인덱스를 정리해준 다음에 visited를 확인해야함
                if visited[ni][nj] ==0:
                    if board[ni][nj] == first:
                        board[i][j] = board[ni][nj] = 0
                        visited[ni][nj] = 1
                        zero += 1
                        q.append([ni, nj])

    return zero

def change(arr):
    total = 0
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                cnt += 1
                total += board[i][j]
    # 0으로 나눠지는 것을 막기 위해서
    if cnt ==0:
        return
    ave = total /cnt
    for i in range(N):
        for j in range(M):
            if board[i][j] !=0:
                if board[i][j] > ave:
                    board[i][j] -= 1
                elif board[i][j] < ave:
                    board[i][j] += 1




# 원판의 개수, 수 개수, 회전 수
N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for x in range(N)]
# 회전정보(원판번호, 방향, 횟수)
infos = [list(map(int, input().split())) for x in range(T)]

while infos:
    info = infos.pop(0)
    n, d, t = info
    for i in range(N):
        if (i+1) % n == 0:
           move(board[i], d, t)
    visited = [[0] * M for x in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] !=0 and visited[i][j] == 0:
                cnt += bfs(i, j)
    # 지울 수 있는 것이 없을 때
    if cnt == 0:
        change(board)

ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            ans += board[i][j]

print(ans)


