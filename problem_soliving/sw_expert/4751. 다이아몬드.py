import sys
sys.stdin=open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    word = input()

    if len(word)==1:
        print('..#..')
        print('.#.#.')
        print('#.'+word+'.#')
        print('.#.#.')
        print('..#..')
    elif len(word) >=2:
        for i in range(len(word)):
            print(('..#.'), end='')
        print('.')
        for i in range(len(word)):
            print(('.#.#'), end='')
        print('.')
        for i in range(len(word)):
            print('#.{}.'.format(word[i]), end='')
        print('#')
        for i in range(len(word)):
            print(('.#.#'), end='')
        print('.')
        for i in range(len(word)):
            print(('..#.'), end='')
        print('.')