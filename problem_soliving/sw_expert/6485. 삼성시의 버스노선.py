import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    check = [0] * 50001
    for i in range(N):
        n1, n2 = map(int, input().split())
        for x in range(n1, n2+1):
            check[x] +=1
    P = int(input())
    ans = []
    for i in range(P):
        c = int(input())
        ans.append(check[c])
    ans = list(map(str, ans))
    print('#{} {}'.format(tc, ' '.join(ans)))
