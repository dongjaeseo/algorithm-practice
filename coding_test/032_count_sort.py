array = [7, 5, 9, 0, 3, 45, 6 , 2, 4, 5, 6, 35, 2,2 ,2, 1]

count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')

'''
계수 정렬은 whole number 정렬에 효과적
백만 이하면 이게 젤 빠르다하네용
데이터의 값이 반복될때 굳굳

대신 때에 따라서 공간복잡도가 높아질수 있다함
'''