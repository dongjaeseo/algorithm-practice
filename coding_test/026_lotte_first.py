def makeseries(series):
    a = ''
    for i in series:
        if i == '0':
            a += '1'
        else:
            a += '0'
    
    series += a
    return series

a, b = map(int, input().split())

count = 0
series = '0'

while True:
    series = makeseries(series)
    count+=1
    if 2**count > max(a,b):
        break

print(series[a-1:b])