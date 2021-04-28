array =  [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <=1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x>=pivot]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))


'''
재귀 함수를 이용하여 퀵정렬을 해보자 ^ㅇ^
개빠르다함 ! 근데 이미 정렬된 상태면 그닥
완전 무작위이고 데이터 양이 방대하면 퀵정렬 써보세용~~
'''