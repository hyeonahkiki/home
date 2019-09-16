import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    dates = list(input().split())
    # stack에 넣고 연산자를 만났을때 빼야하니 생성
    stack = []
    res = ''
    # 연산자를 구분하기 위해 연산자 리스트
    operator = ['+', '-', '*', '/']
    if len(dates) - 1 != dates.index('.'):
        res = 'error'
    if dates[-1] != '.':
        res = 'error'
    for date in dates:
        if date not in operator:
            stack.append(date)
            if date == '.':
                stack.pop()
                res = stack.pop()

        elif date in operator:
            # stack이 2개 이하면 계산이 안되기 때문에
            # stack이 차있다고만 하면 안됨
            if len(stack) < 2:
                res = 'error'
                break
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if date == '+':
                ans = num1 + num2
                stack.append(ans)
            if date == '*':
                ans = num1 * num2
                stack.append(ans)
            if date == '-':
                ans = num1 - num2
                stack.append(ans)
            if date == '/':
                ans = num1 / num2
                stack.append(ans)

    print('#{} {}'.format(tc, res))
