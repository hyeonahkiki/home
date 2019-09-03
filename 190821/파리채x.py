for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    flys = [list(map(int, input().split())) for x in range(n)]
    max_f = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            ans = 0
            for k in range(m):
               for s in range(m):
                    if i+k == j+s:
                        ans += flys[i+k][j+s]
                    elif (i+k) + (j+s) == m-1:
                        ans += flys[i+k][j+s]
            if ans > max_f:
               max_f = ans
    print('#{} {}'.format(tc, max_f))