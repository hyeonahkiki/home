T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = set()
    cnt = 0
    i = 1
    while len(ans) !=10:
        Nums =  i * N
        cnt += 1
        ans.update(str(Nums))
        i += 1
    print('#{} {}'.format(tc, cnt*N))
