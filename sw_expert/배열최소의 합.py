import sys
sys.stdin = open('input.txt', 'r')

# def check(n, k):
#     global minV
#     if n==k:
#         total = sum(res)
#         if minV > total:
#             minV = total
#         return
#     else:
#         for i in range(k):
#             if used[i] != 1:
#                 res[n] = nums[n][i]
#                 used[i] =1
#                 check(n+1, k)
#                 used[i] = 0
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     nums = [list(map(int, input().split())) for x in range(N)]
#     res = [0] * N
#     used = [0] * N
#     minV = 100000
#     check(0, N)
#     print('#{} {}'.format(tc, minV))
