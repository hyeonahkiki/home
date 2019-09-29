import sys

sys.stdin = open('input.txt', 'r')

di = [0, 1]
dj = [1, 0]
ans = 0


def minS(x, y, ans):
    global N, minV
    # 종료조건을 써줘야 한다
    if x == N - 1 and y == N - 1:
        # 그 전까지 더해진 값에 지금의 값을 더해야한다.
        ans += board[x][y]
        if minV > ans:
            minV = ans
        return
    # 최소값보다 커지면 더 보지 않아도 된다
    elif ans > minV:
        return
    else:
        # 오른쪽과 아래로 이동한 값을 정리
        for k in range(2):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                # 함수안에서 더해주는 이유는 나중에 재귀가 돌아올 것을 대비
                minS(ni, nj, ans + board[x][y])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for x in range(N)]
    # 최소값 설정
    minV = 10000
    x = 0
    y = 0
    minS(0,0,0)
    print('#{} {}'.format(tc, minV))
