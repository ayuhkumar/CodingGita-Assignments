# Q43
n = int(input('Half-height: '))
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    for j in range(2 * (n - i)):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end='')
    for j in range(2 * (n - i)):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

# Q44
n = int(input('Half-height: '))
w = 2 * n - 1
for i in range(n):
    for j in range(i):
        print(' ', end='')
    width = w - 2 * i
    for j in range(width):
        if i == 0 or j == 0 or j == width - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(n - 2, -1, -1):
    for j in range(i):
        print(' ', end='')
    width = w - 2 * i
    for j in range(width):
        if i == 0 or j == 0 or j == width - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Q45
n = int(input('Half-height (max 26): '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(1, i + 1):
        print(chr(64 + j), end='')
    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end='')
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(1, i + 1):
        print(chr(64 + j), end='')
    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end='')
    print()

# Q46
n = int(input('Rows: '))
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    value = 1
    for j in range(i + 1):
        print(value, end=' ')
        if j < i:
            value = value * (i - j) // (j + 1)
        else:
            value = value
    print()

# Q47
n = int(input('Size: '))
for i in range(n // 2, n, 2):
    for j in range(n - i):
        print(' ', end='')
    for j in range(i + 1):
        print('*', end='')
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(i + 1):
        print('*', end='')
    print()
for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        print('*', end='')
    print()

# Q48
n = int(input('Size: '))
for i in range(n // 2):
    for j in range(n):
        if i == 0 and j in (1, n - 2) or (i > 0 and j in (0, n - 1)):
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(n // 2):
    for j in range(n):
        if j == i or j == n - 1 - i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Q49
n = int(input('Odd size: '))
for i in range(n):
    for j in range(n):
        if j == i or j == n - 1 - i or i == n // 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Q50
n = int(input('Size: '))
symbol = input('Symbol: ')
for i in range(n):
    for j in range(n):
        print(symbol, end='')
    print()

# Q51
r = int(input('Rows: '))
c = int(input('Columns: '))
for i in range(r):
    for j in range(c):
        if i in (0, r - 1) or j in (0, c - 1):
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Q52
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(i):
        print('+', end='')
    print()
