import sys
sys.stdin = open('input', 'r')

# 방향별로 움직일 좌표주기(왼쪽부터 탐색/ 한칸 전진시 좌표)
order = {
    0: [0, -1, -1, 0],
    1: [-1, 0, 0, 1],
    2: [0, 1, 1, 0],
    3: [1, 0, 0, -1]
}
# 결국 4방향 보게 되는거같은데.....
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 좌표랑 방향
def check(x, y, d):
    global clean
    for key in order.keys():
        if d == key:
            dx, dy = order[d][:2]
            ni = x + dx
            nj = y + dy
            # 왼쪽에 청소할 곳이 있다면
            if 0<=ni<M and 0<= nj <N and space[ni][nj] ==0:
                #바라보는 곳에서 한칸 전진이면
                stepx, stepy = order[d][2:]
                space[ni+stepx][nj+stepy]


# 세로, 가로
N, M = map(int, input().split())
# 좌표랑 방향(0북 1동 2남 3서)
i, j, d = map(int, input().split())
space = [list(map(int, input().split())) for x in range(M)]
# 청소하는 칸의 수
clean = 0
# 현재위치를 청소
if space[i][j] == 0:
    clean += 1
    #탐색할 함수를 실행
    check(i, j, d)