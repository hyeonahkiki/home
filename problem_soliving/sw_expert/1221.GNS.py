import sys
sys.stdin=open('input.txt', 'r')

T= int(input())
for x in range(1, T+1):
    tc, length = input().split()
    N = int(length)
    words = list(input().split())
    translation = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    #각 숫자당 글자가 몇번인지
    cnt = [0] * 10
    for i in range(N):
        word = translation[words[i]]
        cnt[word] += 1

    print(tc)
    for key in translation:
        for i in range(cnt[translation[key]]):
            print(key, end=' ')
