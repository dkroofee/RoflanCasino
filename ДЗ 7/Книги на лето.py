home_library = set()
M = int(input())
home_task = set()
N = int(input())
for i in range(M):
    book = input()
    home_library.add(book)
for i in range(N):
    book = input()
    home_task.add(book)
    if book in home_library:
        print('YES')
    else:
        print('NO')