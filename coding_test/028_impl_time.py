'''
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함된 모든 경우의 수를 구하는 프로그램을 작성하시오.
0 <= N <= 23

5

11475
'''
n = int(input())

timelist = []
for hour in range(n+1):
    for min in range(60):
        for sec in range(60):
            time =  str(hour) + str(min) + str(sec)
            timelist.append(time)

timelist = [num for num in timelist if num.find('3') != -1]
print(len(timelist))