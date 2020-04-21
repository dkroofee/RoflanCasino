people = set()
pause = set()
N = int(input())
M = int(input())
K = int(input())
count = 0
for i in range(N + M + K):
    surname = input()
    if surname in people:
        count += 1
        pause.add(surname)
    people.add(surname)
if (N == M == K) and len(people) == N:
    print('NO')
else:
    if len(pause) + count > 0:
        if (len(pause) + count) % 2 != 0:
            print((len(pause) + count) % 2)
        else:
            print((len(pause) + count) // 2)
    else:
        print('NO')