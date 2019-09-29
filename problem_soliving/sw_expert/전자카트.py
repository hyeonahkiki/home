import sys
sys.stdin = open('input.txt', 'r')

# 순열 만들기
def check(n, k):
    global minV
    if n==k:
        total = 0
        for i in range(k-1):
            total += cost[res[i]][res[i+1]]
        total += cost[res[-1]][0]
        if minV > total:
            minV = total
        return
    else:
        for i in range(1, k):
            if used[i] !=1:
                res[n] = i
                used[i] =1
                check(n+1, k)
                used[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for x in range(N)]
    # 순열을 만들 준비
    res = [0] * N
    used = [0] * N
    #최소비용
    minV = 100000
    # 사무실에서 시작해서 사무실로 돌아와서 끝남
    # 사무실 인덱스가 0. 사용했다고 표시
    res[0] =0
    used[0] = 1
    # 순열함수 실행(주의, 사무실한칸을 표시함)
    check(1, N)
    print('#{} {}'.format(tc, minV))