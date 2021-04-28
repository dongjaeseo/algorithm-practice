'''
n명의 학생 성적 낮은 순
2
홍길동 95
이순신 77
'''

n = int(input())

namescore = []
for _ in range(n):
    name, score = input().split()
    score = int(score)
    namescore.append((name, score))

namescore.sort(key = lambda x:x[1])

for i in namescore:
    print(i[0], end = ' ')
