import sys
sys.stdin = open('input.txt', 'r')

# A의 길이, B의 길이
N, M = input().split()
puzzle = [['.'] * len(N) for x in range(len(M))]
for i in range(len(N)):
    for j in range(len(M)):
        if N[i] == M[j]:
            for k in range(len(N)):
                puzzle[j][k] = N[k]
            break
    if M[j] ==N[i]:
        for s in range(len(M)):
            puzzle[s][i] = M[s]
        break
for i in puzzle:
    print(''.join(i))