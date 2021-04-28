a, b, budget = map(int, input().split())

count = 0

while budget >= 0:
    if budget % a == 0:
        count += 1
    budget -= b

print(count)