import sys
sys.stdin = open('input.txt', 'r')
# 채울칸, 채울 수 있는 수, 구해야하는합, 구한합
def check(n, k, s, m):
    global cnt
    if n==k:
        if s==m:
            cnt +=1
        return
    else:
        # 부분집합에 포함될때
        check(n+1, k, s, m+nums[n])
        # 부분집합에 포함되지 않을때
        check(n+1, k, s, m)



T = int(input())
for tc in range(1, T+1):
    # 원소의 개수, 부분 수열의 합
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    # 경우의 수
    cnt = 0
    check(0, N, 3, 0)
    print('#{} {}'.format(tc, cnt))