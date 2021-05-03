'''
모험가 길드 공포도
5
2 3 1 2 2

2
'''

n = int(input())
members = list(map(int, input().split()))

one = members.count(1)
two = members.count(2)
three = members.count(3)

count = one + two//2 + (three+(two%2)) //3

print(count)