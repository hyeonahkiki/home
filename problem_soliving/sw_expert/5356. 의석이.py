import sys
sys.stdin = open('input.txt', 'r')
def make(text):
    temp = ''
    for i in text:
        if i != '+':
            temp += i
    return temp


T = int(input())

for tc in range(1, T + 1):
    words = [input() for x in range(5)]
    long_word = ''
    ans = []
    for word in words:
        if len(word) > len(long_word):
            long_word = word
    for word in words:
        if len(word) < len(long_word):
            diff = len(long_word) - len(word)
            word += '+' * diff
        ans.append(word)
    res = list(zip(*ans))

    word_ans = ''
    for i in res:
        final = make(i)
        word_ans += final
    print('#{} {}'.format(tc, word_ans))