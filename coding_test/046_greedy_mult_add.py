'''
02984

576

* 혹은 + 를 써서 가장 큰 수 만들기
'''

num = input()

result = 0
for i in num:
    if result == 0:
        result += int(i)
        continue
    if int(i) == 0 or int(i) == 1:
        result += int(i)
    else:
        result *= int(i)

print(result)
