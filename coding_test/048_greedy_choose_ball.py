'''
볼링공 n개 최대무게 m
5 3
1 3 2 3 2

8
'''

n, m = map(int, input().split())

balls = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(i+1,n):
        if balls[i] != balls[j]:
            count += 1

print(count)