array = [2,5,7,9,1,3,4,8,6,0]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)

'''
for 문에서 break가 있기 때문에
이미 어느정도 정렬된 데이터라면 매우 빠르게 동작하기에
삽입 정렬을 쓰는걸 추천해용 >_<~~~
'''