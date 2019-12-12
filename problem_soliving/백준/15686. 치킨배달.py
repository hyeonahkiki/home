import sys

sys.stdin = open('input', 'r')

# M은 최대 치킨집 수
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for x in range(N)]


# 치킨집을 최대 수에 맞춰서 뽑기
def pick(n, k, s, t, arr):
    global minV, total
    if n == s:
        print(res)
        for i in range(len(home)):
            temp = 100000
            for j in range(s):
                h1, h2 = home[i]
                c1, c2 = res[j]
                distance = abs(h1 - c1) + abs(h2 - c2)
                if temp > distance:
                    temp = distance
            total[i] = temp
        if minV > sum(total):
            minV = sum(total)
    else:
        for i in range(t, k):
            if used[i] == 0:
                res[n] = arr[i]
                used[i] = 1
                pick(n + 1, k, s, i + 1, arr)
                used[i] = 0


# 치킨집 위치
chiken = []
home = []
# 치킨거리의 최소값
minV = 100000000
# 총 치킨 거리
for i in range(N):
    for j in range(N):
        if maps[i][j] == 2:
            chiken.append([i, j])
        elif maps[i][j] == 1:
            home.append([i, j])

# 집별로 거리를 입력
total = [0] * len(home)
res = [0] * M
used = [0] * len(chiken)
pick(0, len(chiken), M, 0, chiken)
print(minV)