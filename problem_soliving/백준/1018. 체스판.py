import sys

sys.stdin = open('input', 'r')

# 자신을 중심으로 4방향에 자신과 다른 문자열이 있는지 확인
#  4방향은 같은데 자신만 다르면 cnt +=1
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def check(x, y):
    global N, M
    spot = q.pop(0)
    x = spot[0]
    y = spot[1]
    for k in range(4):
        ni = x + di[k]
        nj = y + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            x, y = ni, nj


# 가로, 세로
N, M = map(int, input().split())
chess = [list(input()) for x in range(M)]
cnt = 0
# 위치를 넣을 장소 필요
q = []
for i in range(N):
    for j in range(M):
        if chess[0][0] == 'W':
            x, y = 0, 0
            q.append([x, y])
