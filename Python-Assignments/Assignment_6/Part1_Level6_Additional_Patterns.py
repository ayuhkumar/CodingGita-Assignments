# Q53
n = int(input('Size: '))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# Q54
n = int(input('Size: '))
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()

# Q55
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        print('*', end='')
    print()

# Q56
n = int(input('Size: '))
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

# Q57
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()

# Q58
n = int(input('Size: '))
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(n - i):
        print('*', end='')
    print()

# Q59
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

# Q60
n = int(input('Size: '))
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(i + 1, n + 1):
        print(j, end=' ')
    print()

# Q61
n = int(input('Size: '))
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(n - i):
        if i == 0 or j == 0 or j == n - i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Q62
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

# Q63
n = int(input('Half-height: '))
w = 2 * n - 1
for i in range(n):
    for j in range(i):
        print(' ', end='')
    width = w - 2 * i
    for j in range(width):
        if j == 0 or j == width - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(n - 2, -1, -1):
    for j in range(i):
        print(' ', end='')
    width = w - 2 * i
    for j in range(width):
        if j == 0 or j == width - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Q64
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()
for i in range(n - 1, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

# Q65
n = int(input('Size (try 3, 5, 7): '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        print('*', end='')
    print()
