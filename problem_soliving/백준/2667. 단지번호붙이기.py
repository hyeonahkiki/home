import sys
sys.stdin = open('input', 'r')


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 반복구조 dfs이용
# def dfs(i, j, n):
#     stack = []
#     home_cnt = 0
#     stack.append([i, j])
#     visited[i][j] = 1
#     while stack:
#         x, y = stack.pop()
#         home_cnt += 1
#         for k in range(4):
#             ni = x + di[k]
#             nj = y + dj[k]
#             if 0<=ni<n and 0<=nj<n and visited[ni][nj] ==0:
#                 if space[ni][nj] == 1:
#                     visited[ni][nj] = 1
#                     stack.append([ni, nj])
#     home.append(home_cnt)

# 재귀 이용
def dfs2(i, j, n):
    global home_cnt
    visited[i][j] = 1
    home_cnt += 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni< n and 0<=nj<n and visited[ni][nj] ==0:
            if space[ni][nj] == 1:
                visited[ni][nj] = 1
                dfs2(ni, nj, n)

N = int(input())
space = [list(map(int, input())) for x in range(N)]
visited = [[0] * N for x in range(N)]
# 단지의 수
cnt = 0
# 각 단지별 집 수
home = []
for i in range(N):
    for j in range(N):
        if space[i][j] ==1 and visited[i][j] ==0:
            # dfs(i, j, N)
            # 재귀 이용할때는 여기에 위치해야함
            home_cnt = 0
            dfs2(i, j, N)
            cnt += 1
            # 재귀가 끝나고 나왔을때 cnt한 것을 넣어야함
            home.append(home_cnt)
print(cnt)
for i in sorted(home):
    print(i)