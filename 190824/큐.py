que =[]
def push(x):
    que.append(x)

def pop():
    if que:
        ans = que.pop(0)
    else:
        ans = -1
    return ans

def size():
    return len(que)

def empty():
    if que:
        return 0
    else:
        return 1

def front():
    if que:
        return que[0]
    else:
        return -1

def back():
    if que:
        return que[-1]
    else:
        return -1
res = []
for tc in range(int(input())):
    word = input()
    if word == 'front':
        res.append(front())
    elif word == 'size':
        res.append(size())
    elif word == 'back':
        res.append(back())
    elif word == 'empty':
        res.append(empty())
    elif word == 'pop':
        res.append(pop())
    else:
        push(word[5:])
ans = list(map(str, res))
print('\n' .join(ans))