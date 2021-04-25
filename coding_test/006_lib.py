# 내장 함수
'''
itertools - 반복되는 형태의 데이터 처리 / 순열과 조합 라이브러리
heapq - 우선순위 큐 기능 구현 / 최단경로 알고리즘
bisect - 이진 탐색 기능
collections - deque, counter 자료구조 포함
math - 수학적 기능 제공
'''

# 내장함수
'''
sum, min, max, eval, sorted
eval > 스트링 형태의 식 계산
sorted > 데이터 리스트 정렬
'''

# 순열과 조합 / Permutation and Combination
'''
순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것 >> npr
조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것 >> ncr = npr / r!
'''

from itertools import permutations, combinations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)
result_com = list(combinations(data, 2))
print(result_com)

# 데이터셋에서 중복허용 n개 데이터 조합이 몇개가 나오는지
from itertools import product

result_prod = list(product(data, repeat = 2))
print(result_prod)

# 데이터셋에서 중복허용 n개 데이터 조합이 몇개가 나오는지 / ('A', 'B') ('B', 'A') 동일간주
from itertools import combinations_with_replacement

result_cwr = list(combinations_with_replacement(data, 2))
print(result_cwr)


# Counter 라이브러리
# collections 라이브러리의 Counter 는 등장 횟수를 세준다
# 리스트에서 내부의 원소가 몇 번씩 등장했는지를 알려줍니다

from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))


# math 라이브러리
# 최대공약수 최소공배수 계산에 효과적

import math
print((lambda a, b: a*b // math.gcd(a, b))(21, 14)) # LCM
print(math.gcd(21, 14))