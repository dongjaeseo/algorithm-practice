# 1부터 9까지 모든 홀수의 합 (while)
i = 1
result = 0

while i <= 9:
    if i%2 ==1:
        result += i
    i += 1

print(result)

# for
# for 변수 in 리스트/튜플:
#     실행문

array = [9, 8, 7, 6, 5]

for x in array:
    print(x)

# range(시작값, 끝값 +1) // 시작값 명시 안할 시 0부터
# >> [시작값 , .... , 끝값]

# continue >> 반복문에서 남은 코드의 실행을 건너뛴다
# >> 포문의 첫줄로 돌아간다
# break >> while for 에서 반복문 즉시탈출

result = 0

for i in range(1, 10):
    if i % 2 == 0:
        continue
    result += i

print(result)

# 응용 : 컨닝한 학생 제외
scores = [90, 85, 100, 54, 99]
cheating_students = {2, 4}

for i in range(5):
    if i in cheating_students:
        continue
    if scores[i] > 80:
        print(f'축하합니다! {i+1}번째 학생은 합격입니다')