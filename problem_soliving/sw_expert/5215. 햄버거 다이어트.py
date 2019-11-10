import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # 재료의 수, 칼로리
    N, L = map(int, input().split())
    info = []
    for x in range(N):
        # 맛에 대한 점수, 칼로리
        T, K = map(int, input().split())
        info.append([T, K])
    ansT = []
    ansK = []
    # 여기서 N은 배열의 길이
    for i in range(1<<N):
        tasty = 0
        kcal = 0
        for j in range(N):
            if i & (1<<j):
                tasty += info[j][0]
                kcal += info[j][1]
        if kcal <=L:
            ansT.append(tasty)
            ansK.append(kcal)
    print('#{} {}'.format(tc, max(ansT)))
