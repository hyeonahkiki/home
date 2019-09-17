import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    subset=[]
    for i in range(1, 1<<7):
        pre = []
        for j in range(7):
            if i & (1<<j):
               pre.append(nums[j])
        subset.append(pre)
    # 중복을 없애기 위해
    subset_S=set()
    for i in subset:
        if len(i) ==3:
            subset_S.add(sum(i))
    subset_S = sorted(subset_S, reverse=True)
    print('#{} {}'.format(tc, subset_S[4]))
