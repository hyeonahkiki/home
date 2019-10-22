import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    many = 0

    for i in range(len(str1)):
        cnt = 0
        if str1[i] in str2:
           cnt += str2.count(str1[i])
        if cnt > many:
            many = cnt
    print('#{} {}'.format(tc, many))