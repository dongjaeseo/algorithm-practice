'''
n에서 1을 뺀다
n 을 k로 나눈다
최소횟수 찾아용~

25 5
2
'''

n, k = map(int, input().split())

count = 0
while n > 1:
    if n%k == 0:
        n //= k
        count +=1
    else:
        count += n%k
        n -= n%k

print(count)