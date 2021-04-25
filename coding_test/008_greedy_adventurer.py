number = int(input())
data = list(map(int, input().split()))

count = 0

count += data.count(1)
count += data.count(2)//2
count += (data.count(2)%2+data.count(3)) // 3

print(count)