import sys
sys.stdin = open('input.txt', 'r')

# 쓴거, 쓸수있는거, 구해야하는 합, 지금까지의 합, 부분집합의 수, 뽑은거 다음
def subset(n, k, s, t, m, z):
    global cnt
    if n==m:
        if s == t:
            cnt += 1
            print(res)
        return
    elif t > s:
        return
    else:
        for i in range(z, N):
            if used[i] != 1:
                used[i] = 1
                res[n] = nums[i]
                subset(n + 1, k, s, t + nums[i],m, i)
                used[i] = 0
    return
# 쓴거, 쓸 수 있는거, 구해야하는거, 지금까지 합
def f(n, k, m, s):
    global cnt
    if n == k:
        if s == m:
            cnt += 1
        return
    else:
        # 부분집합에 포함되는것
        f(n+1, k, m, s + nums[n])
        # 부분집합에 포함되지 않을때
        f(n + 1, k, m, s)

T = int(input())
for tc in range(1, T+1):
    # 수열의 개수, 구해야할 합
    N, K = map(int, input().split())
    # 수열
    nums = list(map(int, input().split()))
    # 경우의 수
    cnt = 0
    # f(0, N, K, 0)
    for i in range(1, N+1):
        res = [0] * N
        used = [0] * N
        subset(0, N, K, 0, i, 0)
    print('#{} {}'.format(tc, cnt))