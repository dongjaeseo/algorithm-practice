'''
i cant die im all in~~~
n 개의 화폐 m 원을 만들거
제일 작은 n코인의 갯수 구해라
불가능하면 -1

2 15
2
3

5

3 4
3
5
7

-1
'''

n, m = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

d = [10001]*10001

d[0] = 0

for i in range(n):
    for j in range(coin[i], m+1):
        if d[j-coin[i]] != 10001:
            d[j] = min(d[j-coin[i]]+1, d[j])

if d[m] == 10001:
    print(-1)
else:
    print(d[m])