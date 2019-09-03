# 날짜계산기

T= int(input())
for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    m_31 = [1, 3, 5, 7, 8, 10, 12]
    m_30 = [4, 6, 9, 11]
    m_28 = [2]

    if m1 != m2:
        d1 + d2 + 1 +  
    else:
        ans = d2 - d1 + 1
    print('#{} {}'.format(tc, ans))
