import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    re_nums = sorted(nums, reverse=True)
    ans= []
    for i in range(N//2+1):
        ans.append(re_nums[i])
        ans.append(re_nums[N - 1 - i])
    res = list(map(str, ans))
    print('#{} {}'.format(tc, ' '.join(res[:10])))