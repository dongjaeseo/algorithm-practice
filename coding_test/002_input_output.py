# input() 한 줄의 문자열을 입력 받는다
# map() 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
# 공백을 기준으로 구분된 데이터를 입력 받을 때
## list(map(int, input().split()))

# 숫자 한 개
n = int(input())

# 숫자들 리스트화
data = list(map(int, input().split()))

print(n, data)


# 입력을 최대한 빠르게 받을 때
# sys.stdin.readline().rstrip()
import sys
data = sys.stdin.readline().rstrip()
print(data)