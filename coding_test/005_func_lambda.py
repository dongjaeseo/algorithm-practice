def add(a, b):
    return a + b

print(add(3, 7))

# global 키워드로 변수를 함수내에서 지정하면
# 해당 함수에서 지역변수 생성 X
# 함수 바깥에 선언된 변수를 바로 참조한다

a = 0
def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# return 은 여러개 가능

# lambda 표현식은 함수를 한 줄로 작성가능
# 이름없는 함수라고도 표현
# 함수를 호출하는 함수일때
# 함수가 간단하거나 한번 사용하고 말때
print((lambda a, b: a + b)(3, 7))

# 자주 사용되는 람다 함수
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

print(sorted(array, key = lambda x:x[1]))

# 자주 사용되는 람다 예시
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a+b, list1, list2)

print(list(result))