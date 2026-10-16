# Q33
n = int(input('Size: '))
for i in range(n):
    for j in range(n):
        if i in (0, n - 1) or j in (0, n - 1):
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Q34
r = int(input('Rows: '))
c = int(input('Columns: '))
for i in range(r):
    for j in range(c):
        if i in (0, r - 1) or j in (0, c - 1):
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Q35
n = int(input('Size: '))
for i in range(n):
    for j in range(n):
        if i in (0, n - 1) or j in (0, n - 1):
            print('1', end='')
        else:
            print('0', end='')
    print()

# Q36
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(i):
        if j == 0 or j == i - 1 or i == n:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Q37
n = int(input('Size: '))
for i in range(n, 0, -1):
    for j in range(i):
        if i == n or j == 0 or j == i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Q38
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        if i == n or j == 0 or j == 2 * i - 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Q39
n = int(input('Half-height: '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Q40
n = int(input('Odd size: '))
for i in range(n):
    for j in range(n):
        if j == i or j == n - 1 - i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Q41
n = int(input('Odd size: '))
for i in range(n):
    for j in range(n):
        if j == i or j == n - 1 - i or i == n // 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Q42
n = int(input('Odd size: '))
for i in range(n):
    for j in range(n):
        if j == i or j == n - 1 - i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
