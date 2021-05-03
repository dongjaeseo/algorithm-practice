from itertools import product

numbers = [1,2,3,4]

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    prod = list(map(sum, product(*l)))
    return prod.count(target)

print(solution(numbers,2))