import sys

sys.stdin = open('input', 'r')


def division(n, k):
    global total
    if n == k:
        return
    else:
        groupA = []
        groupB = []
        for i in range(1, k + 1):
            if used[i] != 1:
                groupA.append(i)
                used[i] = 1
                division(n + 1, k)
                if len(groupA) + len(groupB) == k and len(groupA) * len(groupB) != 0:
                    total.append((groupA, groupB))
                used[i] = 0
            else:
                groupB.append(i)
    return

# 연결된 지역인지 확인하기
def bfs(lists):
    q= [lists[0]]
    visited = [0] * (N+1)
    while q:
        spot = q.pop(0)



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
used = [0] * (N + 1)
total = []
division(0, N)
res = []
for i in total:
    if i not in res:
        res.append(i)
# 최소값
minV = 10000

# 나뉜 구역이 연결된 구역인지 확인하기
for part in res:
    groupA, groupB = part
    print(groupA, groupB)
    ansA = bfs(groupA)
    ansB = bfs(groupB)
    # 각 구역별 인구합
    preA = 0
    preB = 0
    if ansA == True and ansB == True:
        for i in range(len(groupA)):
            preA += info[i]
        for j in range(len(groupB)):
            preB += info[j]
    if minV > abs(preA - preB):
        minV = abs(preA - preB)
# print(minV)
