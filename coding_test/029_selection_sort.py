array = [1,5,3,6,9,8,2,4,7,0]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]

print(array)

'''
선택정렬은 원시적이나 코테에서는 작은 데이터를 찾는일이 잦으므로
익숙해질 필요가 있다!
'''