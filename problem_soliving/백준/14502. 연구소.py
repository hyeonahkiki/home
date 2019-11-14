import sys
sys.stdin = open('input', 'r')

# 벽을 3개씩 뽑는다
    # ====== 반복 =======
    # spot => 하나씩뽑아서 벽을 세운다
    # 바이러스 퍼트린다 check visited 초기화
    # 벽을 제거한다

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 바이러스 퍼뜨릴 함수
def check():
    global spotZ, N, M, visited, zero, virus, cntZ, maxV
    visited = [[0] * M for _ in range(N)]
    q = [0] * N * M
    front = rear = -1
    # 0인것만 바이러스에 감염되니까 q에 들어간 것은 감염된것.
    cnt = 0
    for v in virus:
        rear += 1
        q[rear] = v
    while front != rear:
        front += 1
        # 바이러스 위치를 빼기
        i, j = q[front]
        visited[i][j] = 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] ==0 and lab[ni][nj] == 0:
                visited[ni][nj] = 1
                rear += 1
                cnt += 1
                q[rear] = [ni, nj]
    # 벽을 세우는 3개를 빼야함...
    if maxV < cntZ-cnt-3:
        maxV = cntZ-cnt-3
    return maxV

# 가로, 세로
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for x in range(N)]
maxV = 0


# 0의 좌표값을 다 담아서 가기
zero = []
virus = []
for i in range(N):
    for j in range(M):
        if lab[i][j]==2:
            virus.append((i, j))
        elif lab[i][j] == 0:
            zero.append([i, j])
cntZ = len(zero)

# 0좌표를 세개씩 뽑기
spotZ = []
for a in range(0, len(zero)-2):
    for b in range(a+1, len(zero)-1):
        for c in range(b+1, len(zero)):
            spotZ.append([a, b, c])



# 벽 먼저 세우기
for a in range(len(spotZ)):
    # zero에서 쓰일 인덱스를 뽑기
    s1, s2, s3 = spotZ[a]
    # 벽 세울 위치 3개
    x1, y1 = zero[s1]
    x2, y2 = zero[s2]
    x3, y3 = zero[s3]
    # 일단 벽 세우기
    lab[x1][y1] = 1
    lab[x2][y2] = 1
    lab[x3][y3] = 1
    # 바이러스 퍼뜨리기
    check()
    # 다시 세야하니까 벽도 원래대로
    lab[x1][y1] = 0
    lab[x2][y2] = 0
    lab[x3][y3] = 0
print(maxV)