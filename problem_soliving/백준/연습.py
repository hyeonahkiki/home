import sys

sys.stdin = open('input', 'r')

# 세로크기, 가로크기
N, M = map(int, input().split())
board = [list(map(int, input().split())) for x in range(N)]
maxV = -1
# 정사각형
for i in range(M-2):
    for j in range(N-1):
        s1 = 0
        for k in range(2):
            for s in range(2):
                s1 += board[i+k][j+s]
        if s1 > maxV:
            maxV = s1

#  일자(가로)
for i in range(N):
    for j in range(M - 4 + 1):
        s2 = 0
        for k in range(4):
            s2 += board[i][j + k]
        if s2 > maxV:
            maxV = s2

#  일자(세로)
for i in range(N - 4 + 1):
    for j in range(M):
        s3 = 0
        for k in range(4):
            s3 += board[i + k][j]
        if s3 > maxV:
            maxV = s3
#
# # ㄱ자 모양
for i in range(M - 3 + 1):
    for j in range(N - 2):
        s4 = 0
        for k in range(3):
            s4 += board[i][j + k]
            if k == 2:
                s4 += board[i + 1][j + k]
        if s4 > maxV:
            maxV = s4

# # ㄱ자 뒤집어진거
for i in range(M - 3 + 1):
    for j in range(N - 2):
        s5 = 0
        for k in range(3):
            s5 += board[i][j + k]
            if k == 0:
                s5 += board[i + 1][j + k]
        if s5 > maxV:
            maxV = s5

# # ㄴ자
for i in range(1, M - 3 + 1):
    for j in range(N - 2):
        s6 = 0
        for k in range(3):
            s6 += board[i][j + k]
            if k == 0:
                s6 += board[i - 1][j + k]
        if s6 > maxV:
            maxV = s6

#  ㄴ자 뒤집어진거
for i in range(1, M - 3 + 1):
    for j in range(N - 2):
        s7 = 0
        for k in range(3):
            s7 += board[i][j + k]
            if k == 2:
                s7 += board[i - 1][j + k]
        if s7 > maxV:
            maxV = s7

# 5이거 비슷한모양
for i in range(M - 3):
    for j in range(N-1):
        s8 = 0
        for k in range(2):
            s8 += board[i + k][j]
            if k == 1:
                s8 += board[i + k][j + 1]
                s8 += board[i + k + 1][j + 1]
        if s8 > maxV:
            maxV = s8
#
# 5이거 뒤집은거
for i in range(M - 3):
    for j in range(1, N - 2):
        s9 = 0
        for k in range(2):
            s9 += board[i + k][j]
            if k == 0:
                s9 += board[i + k + 1][j - 1]
                s9 += board[i + k + 2][j - 1]
        if s9 > maxV:
            maxV = s9

# ㄹ자 모양
for i in range(M - 2):
    for j in range(N-2):
        s10 = 0
        for k in range(2):
            s10 += board[i][j + k]
            if k == 1:
                s10 += board[i + 1][j + k]
                s10 += board[i + 1][j + k + 1]
        if s10 > maxV:
            maxV = s10

# ㄹ자 뒤집어진 모양
for i in range(1, M - 1):
    for j in range(N - 2):
        s11 = 0
        for k in range(2):
            s11 += board[i][j + k]
            if k == 1:
                s11 += board[i - 1][j + k]
                s11 += board[i - 1][j + k + 1]
        if s11 > maxV:
            maxV = s11

# ㅜ 모양
for i in range(M - 2):
    for j in range(N - 2):
        s12 = 0
        for k in range(3):
            s12 += board[i][j + k]
            if k == 1:
                s12 += board[i + 1][j + k]
        if s12 > maxV:
            maxV = s12

# ㅗ모양
for i in range(1, M - 2):
    for j in range(N - 2):
        s13 = 0
        for k in range(3):
            s13 += board[i][j + k]
            if k == 1:
                s13 += board[i - 1][j + k]
        if s13 > maxV:
            maxV = s13

# ㅏ모양
for i in range(M - 3):
    for j in range(N-1):
        s14 = 0
        for k in range(3):
            s14 += board[i + k][j]
            if k == 1:
                s14 += board[i + k][j + k]
        if s14 > maxV:
            maxV = s14

# ㅓ모양
for i in range(M - 3):
    for j in range(1, N):
        s15 = 0
        for k in range(3):
            s15 += board[i + k][j]
            if k == 1:
                s15 += board[i + k][j - k]
        if s15 > maxV:
            maxV = s15

# 긴 ㄱ모양뒤집은거
for i in range(M - 3):
    for j in range(N-1):
        s16 = 0
        for k in range(3):
            s16 += board[i + k][j]
            if k == 0:
                s16 += board[i + k][j + 1]
        if s16 > maxV:
            maxV = s16

# 긴 ㄱ모양
for i in range(M - 3):
    for j in range(1, N):
        s17 = 0
        for k in range(3):
            s17 += board[i + k][j]
            if k == 0:
                s17 += board[i + k][j + k - 1]
        if s17 > maxV:
            maxV = s17

# 긴 ㄴ자모양
for i in range(M - 3):
    for j in range(N-1):
        s18 = 0
        for k in range(3):
            s18 += board[i + k][j]
            if k == 2:
                s18 += board[i + k][j + k - 1]
        if s18 > maxV:
            maxV = s18

# 긴 ㄴ자 모양 뒤집은거
for i in range(M - 3):
    for j in range(1, N):
        s19 = 0
        for k in range(3):
            s19 += board[i + k][j]
            if k == 2:
                s19 += board[i + k][j + k - 3]
        if s19 > maxV:
            maxV = s19
print(maxV)
