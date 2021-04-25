# 스택은 입출구가 같은 데이터자료형태 / 마지막으로 들어온게 먼저 나간다
# 이는 파이썬에서 리스트로 간단히 구현 가능
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])
print(stack)

# 큐는 먼저 들어온 데이터가 먼저 나가는 형식의 자료구조
# 양쪽이 뚫려있는 터널 형태
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# 재귀 함수 > 자기 자신을 다시 호출하는 함수
def recursive_function(i):
    if i == 100:
        return
    print(f'{i}th recur_func calling {i+1}th recur func')
    recursive_function(i+1)
    print(f'{i}th recursive_function ends')

recursive_function(1)


# recusive function - calculating factorials
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))

# GCD algorithm using recursive function
def GCD(a, b):
    if a%b == 0:
        return b
    else:
        return GCD(b, a%b)

print(GCD(30, 12))




