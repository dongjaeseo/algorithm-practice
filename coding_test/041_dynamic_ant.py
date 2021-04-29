'''
일직선 식량창고 
'''

n = int(input())
food = list(map(int, input().split()))

d = [0]*100

d[0] = food[0]
d[1] = max(food[1],food[0])

for i in range(2, n):
    d[i] = max(d[i-2]+food[i], d[i-1])

print(d[n-1])