import sys

sys.stdin = open('input.txt', 'r')

# 인덱스랑 그 전인덱스까지의 합이 같아야한다.

T = int(input())
for tc in range(1, T+1):
    clap = list(map(int, input()))
    # 사람 수를 저장
    human = 0
    # 고용할 사람 수
    hire = 0
    for i in range(0, len(clap)):
        if clap[i] !=0:
            if i >= human:
              hire += i - human
              human += i-human
              human += clap[i]
            else:
                human +=clap[i]

    print('#{} {}'.format(tc, hire))
