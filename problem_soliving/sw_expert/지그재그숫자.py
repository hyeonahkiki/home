import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = [x for x in range(1, N+1)]
    ans = 0
    for i in range(N):
        if nums[i] %2:
            ans += nums[i]
        else:
            ans -= nums[i]
    print('#{} {}'.format(tc,ans))