import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # 재료수, 제한 칼로리
    N, L = map(int, input().split())
    info = []
    for i in range(N):
        T, K = map(int, input().split())
        info.append([T, K])
    # 만들 수 있는 모든 조합을 찾은 후에 max값 찾기
    best = 0
    # 햄버거 만들기
    tasty = []

    for j in range(len(info)):
        limit = 0
        score = 0
        for k in range(0, j+1):
            score += info[j][0]
            limit += info[j][1]
            if limit >L:
                break
    print(max(tasty))
