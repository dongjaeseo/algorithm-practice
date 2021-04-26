# 얼음틀 dfs를 활용한 풀이
'''
첫 번째 줄에 얼음틀의 세로 길이와 가로 길이가 주어집니다 (N, M)
두번째 줄부터 N+1 전째 줄까지 얼음 틀의 형태가 주어집니다
이 때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다

입력예시:
4 5
00110
00011
11111
00000
'''

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y > n:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        print(f'{i},{j},{dfs(i,j)}')
        if dfs(i, j) == True:
            result += 1

print(result)