import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    # 곱한 수를 담는다
    cals = []
    # 최대값 설정
    maxV = -1
    ans = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            ans = str(nums[i] * nums[j])
            for k in range(len(ans) - 1):
                if int(ans[k + 1]) < int(ans[k]):
                    break
            else:
                if maxV < int(ans):
                    maxV = int(ans)
    print('#{} {}'.format(tc, maxV))