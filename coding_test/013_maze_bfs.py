# BFS 를 활용한 미로 최단루트 찾기 알골즘
'''
BFS는 주로 미로 최단거리 찾는 알고리즘에서 사용된다
시작지점에서 가장 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색한다
따라서 1, 1 지점에서 BFS를 수행하여 모든 노드의 최단거리값을 기록하면 해결할 수 있다
'''

from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                print(graph[nx][ny], nx, ny)
                queue.append((nx, ny))
    return graph[n -1][m - 1]

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))
