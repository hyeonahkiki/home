# n: 현재호출에서 접근할 원소의 인덱스, k: 배열의 크기
# def f(n, k):
#     if n==k:
#         print(a[n])
#     else:
#         f(n+1, k)
#
a= [1, 2, 3]
b = [0, 0, 0]
# f(0, 2)

# 재귀로 집합 a의 부분집합 만들기
def f2(n, k):
    # b배열을 벗어나면
    if n==k:
        for n in range(k):
            if b[n] ==1:
                print(b[n], end="")
        print()
    else:
        # 남은 원소가 있으면
        b[n] = 0
        f2(n+1, k)
        b[n] = 1
        f2(n+1, k)

# 서로 다른 k개의 자연수의 지합에서 부분집합 원소의 합이 M인 경우의 수
cnt = 0
def f3(n, k, s, m):
    global cnt
    if s==m:
        cnt += 1
        return
    elif n==k:
        return
    else:
        # 부분집합에 a[n] 포함
        f3(n + 1, k, s + a[n], m)
        # 부분집합에 a[n] 미포함
        f3(n+1, k, s, m)