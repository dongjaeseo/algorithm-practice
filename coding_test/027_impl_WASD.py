'''
n,n 맵에서 움직임을 줬을때 마지막 좌표값 구하기
대신 밖으로 나가려는 움직임 무시
'''

map_size = int(input())

move_dict = {
    'U':[-1,0],
    'R':[0,1],
    'L':[0,-1],
    'D':[1,0]
}

initial_pos = [1,1]

moves = list(input().split())

for move in moves:
    for i in range(2):
        initial_pos[i] += move_dict[move][i]
    if initial_pos[0]<=0 or initial_pos[0]>map_size or initial_pos[1]<=0 or initial_pos[1]>map_size:
        for i in range(2):
            initial_pos[i] -= move_dict[move][i]

print(initial_pos[0], initial_pos[1])