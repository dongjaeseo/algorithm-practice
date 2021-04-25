# x in 리스트 형태로 리스트안에 x의 유무 판단

x = 2
if x in [1,2,3]:
    print('True')

# pass 키워드는 보통 조건문에서 수행할 코드 작성은 나중에 하고 싶을때 사용

a = 20

if a >=30:
    pass
else :
    print('a < 30')

# 조건문의 간소화
score = 85
if score >= 80: result = 'Success'
else: result = 'Fail'
print(result)

# 조건문의 간소화2
score = 85
result = 'Success' if score >=80 else 'Fail'
print(result)

x = 15
print(0<x<=20) 