# n = 10
# array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# array = [1,2,3,4,5,6,7,8,9,10]
n = 6
array = [4, 1, 7, 6, 5, 2]


def find(n, array):
    small_array = []
    for i in range(n-1):
        small_array.append(array[i:])
    
    temp = small_array[0][0] - min(small_array[0][1:])
    for i in small_array:
        if temp < i[0]-min(i[1:]):
            temp = i[0]-min(i[1:])
    
    print(temp)

    
find(n, array)