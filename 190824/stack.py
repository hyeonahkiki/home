# 백준- 스택(1874)
tc = int(input())
final = [int(input()) for x in range(tc)]
stack=[]
sign = []
i = 0
for t in range(1, tc+1):
    stack.append(t)
    sign.append('+')

    for n in range(len(stack)):
        if stack[-1] == final[i]:
            stack.pop()
            sign.append('-')
            i += 1
        else:
            break

if stack:
   print('NO')
else:
    print('\n' ''.join(sign))