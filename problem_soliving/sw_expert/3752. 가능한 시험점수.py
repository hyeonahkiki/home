import sys
sys.stdin = open('input.txt', 'r')

def check(n, k, s, t):
    global ans, cnt
    cnt += 1
    for i in range(t, k):
        if used[i] ==0:
            used[i] = 1
            check(n+1, k, s+score[i], i)
            ans.add(s)
            used[i] = 0
    ans.add(s)

# def check(n, k, s):
#     global ans, cnt
#     cnt += 1
#     if n == k:
#         ans.add(s)
#     else:
#         check(n+1, k, s+score[n])
#         check(n+1, k, s)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    ans = set()
    used = [0] * N
    cnt = 0
    # check(0, N, 0)
    check(0, N, 0, 0)
    print(ans, cnt)
    print('#{} {}'.format(tc, len(ans)))
