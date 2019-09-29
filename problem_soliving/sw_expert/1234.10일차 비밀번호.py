import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, 2):
    N, password = input().split()
    ans = []
    for i in range(int(N)):
        if password[i] not in ans:
            ans.append(password[i])
        elif password[i] == ans[-1]:
            ans.pop(-1)
        else:
            ans.append(password[i])
    print('#{} {}'.format(tc, ''.join(ans)))
