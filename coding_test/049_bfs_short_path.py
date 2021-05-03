'''
4 4 2 1
1 2
1 3
2 3
2 4
'''
from collections import deque

n, m, k, x = map(int, input().split())

graphs = []
for i in range(1, m+1):
    graphs.append(list(map(int, input().split())))
visited = [False]*(n+1)
distance = [0]*(n+1)

def find(graph, start, visited, k, distance):
    queue = deque([start])
    visited[start] = True
    while queue:
        n = queue.popleft()
        for graph in graphs:
            if graph[0] == n:
                if visited[graph[1]] == False:
                    queue.append(graph[1])
                    distance[graph[1]] = distance[n] + 1
                    visited[graph[1]] = True
    
    count = 0
    for n, i in enumerate(distance):
        if i==k:
            count = 1
            print(n)
    
    if count == 0:
        print(-1)
                
find(graphs, x, visited, k, distance)        
            
