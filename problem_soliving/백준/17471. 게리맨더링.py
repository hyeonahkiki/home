import sys
sys.stdin = open('input', 'r')

def division(n, k):
    global total
    if n==k:
        return
    else:
        groupA = []
        groupB = []
        for i in range(1, k+1):
            if used[i] != 1:
                groupA.append(i)
                used[i] = 1
                division(n+1, k)
                if len(groupA) + len(groupB) == k:
                    total.append((groupA, groupB))
                used[i] = 0
            else:
                groupB.append(i)
    return

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def bfs(arr):
    if len(arr):
        return True
    else:
        pass

N = int(input())
info = list(map(int, input().split()))
regions = [list(map(int, input().split())) for x in range(N)]

# 인접한 지역을 표시
check = [[0] * (N+1) for x in range(N+1)]
for i in range(N):
    spot = regions[i]
    for j in range(1, spot[0]+1):
        check[i+1][spot[j]] = 1

# 구역을 나누기
used = [0] * (N+1)
total = []
division(0, N)
res = []
for i in total:
    if i not in res:
        res.append(i)

# 나뉜 구역이 연결된 구역인지 확인하기
for part in res:
    groupA, groupB = part
    print(groupA, groupB)
