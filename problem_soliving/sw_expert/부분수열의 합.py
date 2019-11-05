import sys
sys.stdin = open('input.txt', 'r')

# 채운칸, 채울 수 있는 칸, 구해야하는합, 지금까지의 합
def check(n, k, s, m):
    # 개수 세기
    global cnt
    if n==k:
        if s==m:
            cnt += 1
        return
    else:
        # 부분집합에 포함될때
        check(n+1, k, s, m+nums[n])
        # 부분집합에 포함되지 않을때
        check(n+1, k, s, m)


# 주어진 칸을 다 돌아야하니까. n+1을 계속해줌
# 결국 0(넣지않거나) 1(넣거나)해서 두가지의 경우가 계속됨
# 여기서는 4칸을 0으로 채우거나 1을 채우거나해서 어쨌든 4칸을 다 채워야함
# n이 인덱스와 같은 느낌. 그자리에 1이면 인덱스로 보면 됨



T = int(input())
for tc in range(1, T+1):
    # 원수의 개수, 구해야하는 합
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = 0
    check(0, N, K, 0)
    print('#{} {}'.format(tc, cnt))
