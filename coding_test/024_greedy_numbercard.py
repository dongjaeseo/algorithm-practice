'''
카드가 n, m 형태로있을때
한 행을 찝어서 카드를 뽑으면
그 행에서 제일 낮은 숫자가 뽑힌다
이때 뽑을수있는 제일 높은 숫자카드?

3 3
3 1 2
4 1 4
2 2 2

2
'''
n, m = map(int, input().split())

cards = []
for i in range(n):
    cards.append(list(map(int, input().split())))

max_num = 0
for i in range(n):
    temp = min(cards[i])
    if max_num<temp:
        max_num = temp

print(max_num)