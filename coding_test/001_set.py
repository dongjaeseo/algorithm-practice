# 집합 자료형
# 순서가 없다 // 인덱싱 사용 불가
# | & 등으로 교집합 합집합 가능

data = set([1,2,3])
print(data)

# 원소 추가 // 리스트 불가
data.add(7)
print(data)

# 리스트를 추가
data.update([4,5])
print(data)

# 원소 삭제 // 리스트 불가
data.remove(4)
print(data)
