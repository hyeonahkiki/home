import sys

sys.stdin = open('input', 'r')

# 8방향 돌아줄것을 정리
di = [-1, -1, -2, 2, 1, 1, 2, -2]
dj = [-2, 2, 1, 1, 2, -2, -1, 1]


def check():
    global visited, r1, c1, r2, c2, cnt

    q = [0] * 95
    front = -1
    rear = -1
    rear += 1
    q[rear] = [r1, c1]
    visited[r1][c1] = 1
    while front != rear:
        front += 1
        spot = q[front]
        i = spot[0]
        j = spot[1]
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 10 and 0 <= nj < 9 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                cnt[rear] += 1
                if ni == r2 and nj ==c2:
                    return cnt
                else:
                    cnt[rear] = 0
                    rear += 1
                    q[rear] = [ni, nj]


# 상의 위치
r1, c1 = map(int, input().split())
# 왕의 위치
r2, c2 = map(int, input().split())
# 장기판 생성
visited = [[0] * 9 for x in range(10)]
# 몇번만에 왕에 도달하는지
cnt = [0] * 95
check()
print(max(cnt))
