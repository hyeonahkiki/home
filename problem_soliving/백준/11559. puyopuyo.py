import sys
sys.stdin = open('input', 'r')

# 12 * 6의 문자가 주어진다
# 상하좌우 4개 이상 모이게 되면 또 터진다.
# 터질 수 있는 뿌요가 여러그룹이라면 동시에 터지고
# 한번의 연쇄가 추가

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
# 좌표, 무슨 문자열인지
def check(x, y, w):
    global total
    # 터뜨린 경우
    broken = 0
    q= [0] * 12 * 6
    visited = [[0] * 6 for x in range(12)]
    front = rear = -1
    rear += 1
    q[rear] = [x, y]
    visited[x][y] = 1
    # 상하좌우가 같은 문자열인지 확인해야함
    cnt = 1

    while front != rear:
        front += 1
        i, j = q[front]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<= ni < 12 and 0<=nj<6 and visited[ni][nj] ==0:
                if game[ni][nj] == w:
                    cnt += 1
                    visited[ni][nj] = 1
                    rear += 1
                    q[rear] = [ni, nj]

    if cnt >=4 :
        broken+=1
        for s in range(12):
            for t in range(6):
                if visited[s][t] != 0:
                    game[s][t] = '.'

    # 터뜨린게 없는 경우
    if broken ==0:
        return game, False
    else:
        return game, True

def drop(arr):
    # 세로로 보면서 밑에서 부터 올라온다
    # .이 아닌거랑 .인거랑 위치 바꿔주기
    # 밑으로 내려야 하니까 밑에부터 보기
    for j in range(6):
        # 밑에서 부터 탐색
        for i in range(12-1, -1, -1):
            if arr[i][j] == '.':
                # 어차피 맨 마지막은 탐색을 했으니까 그 위에 부터 탐색
                for k in range(i-1, -1, -1):
                    if arr[k][j] != '.':
                        arr[i][j], arr[k][j] = arr[k][j], arr[i][j]
                        # 자리를 바꾼후에 break안걸면 그 위로 올라가면서 또 자리를 바꾸는 상황발생
                        break
    return arr





game = [list(input()) for x in range(12)]
# print(game)

# 총 몇 연쇄인지
total = 0

# 우선 문자열 찾기
# 더이상 터뜨릴게 없을때까지 돌리기 위해서
while 1:
    ans = 0
    # 밑에서부터 탐색
    for i in range(12-1, -1, -1):
        for j in range(6):
            if game[i][j] != '.':
                game, res = check(i, j, game[i][j])
                # 터뜨린게 있는경우
                if res:
                    ans += 1
    # 다시 터트릴거 있나 탐색 후에
    # 게임을 하고 밑으로 내려야함
    drop(game)
    # 더 이상 터뜨릴게 없는 경우
    if ans == 0:
        break
    # 하나도 안 터질때는 더해지지 않기 위해서
    # 하나도 안터지는 경우는 break에 걸려서 걸러짐
    # 연쇄도 있기때문에 터질때마다 더해지면 안됨
    total += 1
print(total)

# import sys
#
# sys.stdin = open('input', 'r')
#
#
# def DFS(i, j):
#     global field, visited, count
#
#     d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#
#     visited[i][j] = 1
#     path = [(i, j)]
#     stack = [(i, j)]
#     color = field[i][j]
#     while stack:
#         i_, j_ = stack.pop()
#
#         for dx, dy in d:
#             ni = i_ + dx
#             nj = j_ + dy
#
#             if 0 <= ni < 12 and 0 <= nj < 6:
#                 if field[ni][nj] == color and visited[ni][nj] == 0:
#                     visited[ni][nj] = 1
#                     path.append((ni, nj))
#                     stack.append((ni, nj))
#
#     if len(path) >= 4:  # 각각을 폭발시킨다
#         for i_, j_ in path:
#             field[i_][j_] = '.'
#         count += 1
#         return
#
#
# # 해당 col을 정렬한다
# def align(col):
#     global field
#
#     column = ''
#
#     # 해당 열 복사하기
#     for i in range(12):
#         value = field[i][col]
#         column += value
#
#     column = column.replace('.', '')
#     padding = 12 - len(column)
#     column = '.' * padding + column
#
#     if padding != 0:
#         for i in range(12):
#             field[i][col] = column[i]
#
#
# field = [list(input()) for _ in range(12)]
# boom = 0
#
# while True:
#     visited = [[0] * 6 for _ in range(12)]
#     count = 0  # 폭발하는 군집 수
#     for i in range(12):
#         for j in range(6):
#             if field[i][j] in ['R', 'G', 'B', 'P', 'Y'] and visited[i][j] == 0:
#                 DFS(i, j)  # 군집 찾아 폭발
#
#     # 각 열들을 다시 정렬
#     for i in range(6):
#         align(i)
#
#     if count == 0:  # 폭발한게 하나도 없으면 끝
#         break
#     else:
#         boom += 1
#
# print(boom)
