import sys

sys.stdin = open('input.txt', 'r')

# 인덱스, 비용합, 1일, 1달, 3달
def check(n, s, d, m, m3):
    global minV
    if n >12:
        if minV > s:
            minV = s
    elif minV <s:
        return
    else:
        # 1일권
        check(n+1, s+month[n] * d, d, m, m3)
        # 1달권
        check(n+1, s+m, d, m, m3)
        # 3달권
        check(n+3, s+m3, d, m, m3)


T = int(input())
for t in range(1, T + 1):
    # 1일, 1달, 3달, 1년
    d, m, m3, y = list(map(int, input().split()))
    month = [0]+list(map(int, input().split()))
    minV = y
    check(0, 0, d, m, m3)
    print('#{} {}'.format(t, minV))