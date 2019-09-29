for tc in range(1, int(input())+1):
    m1, d1, m2, d2 = map(int, input().split())
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if m1 != m2:
        cnt = 0
        for j in range(m1+1, m2+1):
            cnt += days[j]
            ans = cnt + (d2-d1+1)
    else:
        ans = d2-d1+1

    print('#{} {}'.format(tc, ans))
