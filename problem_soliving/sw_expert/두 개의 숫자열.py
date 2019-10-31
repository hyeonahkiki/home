import sys
sys.stdin = open('input.txt', 'r')

# n < m
def check(n, m):
    global maxV
    for i in range(m-n+1):
        s = 0
        for k in range(n):
            s += (nums1[k] * nums2[i+k])
        if s > maxV:
            maxV = s
    return maxV

T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    maxV = -10000
    if N < M:
       ans = check(N, M)
    else:
       ans = check(M, N)
    print('#{} {}'.format(tc, ans))