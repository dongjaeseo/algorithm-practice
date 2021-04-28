'''
첫째 줄에 N, M, K
둘째 줄에 N개의 자연수
입력으로 주어지는 K는 항상 M보다 작거나 같다
'''

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

mod, rem = divmod(m, k+1)

print((numbers[-1]*k+numbers[-2])*mod + rem*numbers[-1])