# 채운 칸수, 채울 칸수, 시작점
def check(n, k, s):
    global N, M

    if n==k:
        print(res)
    else:
        for i in range(s, N):
            if used[i] !=1:
                res[n] = i
                used[i] =1
                check(n+1, k, s+1)
                used[i] =0

a = [1, 2, 3, 4, 5]
N = 5
M = 3
used = [0] * N
res = [0] * M
check(0, M, 0)