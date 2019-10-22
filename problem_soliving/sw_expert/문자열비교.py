import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    ans = 0
    for i in range(len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            ans = 1
    print('#{} {}'.format(tc,ans))