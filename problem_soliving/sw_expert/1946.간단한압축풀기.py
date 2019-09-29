T = int(input())
for tc in range(1, T+1):
    N = int(input())
    words = ''
    for x in range(N):
        word, num = input().split()
        words += word * int(num)
    print('#{}'.format(tc))
    for z in range((len(words)//10)+1):
        print('{}'.format(words[z*10:z*10+10]))