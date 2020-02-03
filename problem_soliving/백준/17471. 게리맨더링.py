import sys

sys.stdin = open('input', 'r')


# def division(n, k):
#     global total
#     if n == k:
#         return
#     else:
#         groupA = []
#         groupB = []
#         for i in range(1, k + 1):
#             if used[i] != 1:
#                 groupA.append(i)
#                 used[i] = 1
#                 division(n + 1, k)
#                 if len(groupA) + len(groupB) == k and len(groupA) * len(groupB) != 0:
#                     total.append((groupA, groupB))
#                 used[i] = 0
#             else:
#                 groupB.append(i)
#     return

# n: 시작점 k: groupA의 길이 s: groupA의 리스트, z는 시작점(중복없이 뽑기 위함)
def division(n, k, s, z):
    global total, N
    if n == k:
        b = []
        # 전체리스트 중에 v
        for v in list(range(1, N+1)):
            # v가 나눠진 그룹안에 없다면
            if v not in s:
                b.append(v)
        total.append([s, b])
        return
    else:
        for i in range(z, N+1):
            if used[i] != 1:
                used[i] = 1
                division(n + 1, k, s +[i], i)
                used[i] = 0
    return




# 연결된 지역인지 확인하기
def bfs(lists):
    if len(lists)==1:
        return True
    q = [lists[0]]
    history =[]
    while q:
        spot = q.pop(0)
        visited[spot] = 1
        history.append(spot)
        for i in range(1, N+1):
            if check[spot][i] ==1 and visited[i] ==0 and i in lists:
                q.append(i)
                visited[i] = 1
    # print(history, lists)
    if set(history) == set(lists):
        return True
    return False


N = int(input())
info = list(map(int, input().split()))
regions = [list(map(int, input().split())) for x in range(N)]

# 인접한 지역을 표시
check = [[0] * (N + 1) for x in range(N + 1)]
for i in range(N):
    spot = regions[i]
    for j in range(1, spot[0] + 1):
        check[i + 1][spot[j]] = 1

# 구역을 나누기
total = []
# groupA를 3개뽑면 나머지는 groupB가 나눠진다.
for i in range(1, N//2):
    groupB = []
    used = [0] * (N + 1)
    division(0, i, [], 1)

# 최솟값
minV = 1000000

# 나뉜 구역이 연결된 구역인지 확인하기
for part in total:
    groupA, groupB = part
    visited = [0] * (N + 1)
    ansA = bfs(groupA)
    ansB = bfs(groupB)
    if ansA ==True and ansB ==True:
        cntA = 0
        cntB = 0
        for i in groupA:
            cntA += info[i-1]
        for j in groupB:
            cntB += info[j-1]
        if minV > abs(cntA-cntB):
            minV = abs(cntA-cntB)
if minV == 1000000:
    minV = -1
print(minV)


