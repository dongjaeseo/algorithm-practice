'''
a b 두 리스트 n 길이만큼
k 만큼 원소 교체 후 a 값 최대값 출력

5 3
1 2 5 4 3
5 5 6 6 5
'''

n, k = map(int,input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))