import sys

sys.stdin = open('input.txt', 'r')


# 거리를 구하는 함수
def get_distance(x, y):
    global roads
    i = roads[x][0]
    j = roads[x][1]
    k = roads[y][0]
    s = roads[y][1]
    distance = abs(i - k) + abs(j - s)
    return distance


# 채운거, 채울 수 있는거
def check(n, k):
    global minV
    if n == k:
        cnt = 0
        for i in range(len(go) - 1):
            cnt += get_distance(go[i] + 2, go[i + 1] + 2)
        cnt += get_distance(0, go[0] + 2) + get_distance(1, go[-1] + 2)
        if minV > cnt:
            minV = cnt
        return
    else:
        for i in range(N):
            if used[i] != 1:
                used[i] = 1
                go[n] = i
                check(n + 1, k)
                used[i] = 0
        return


T = int(input())
for tc in range(1, T + 1):
    # 고객 수
    N = int(input())
    # 가야할 길
    pre = list(map(int, input().split()))
    # 좌표를 두개씩 묶기
    roads = []
    minV = 1000000
    for i in range(0, len(pre) - 1, 2):
        roads.append([pre[i], pre[i + 1]])
    # 만들 경로판 만들기
    go = [0] * N
    used = [0] * N
    check(0, N)
    print('#{} {}'.format(tc, minV))
