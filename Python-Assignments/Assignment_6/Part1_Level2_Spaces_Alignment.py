# Q13
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

# Q14
n = int(input('Size: '))
for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

# Q15
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        print('*', end='')
    print()

# Q16
n = int(input('Size: '))
for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        print('*', end='')
    print()

# Q17
n = int(input('Half-height: '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        print('*', end='')
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i - 1):
        print('*', end='')
    print()

# Q18
n = int(input('Size: '))
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(n):
        print('*', end='')
    print()

# Q19
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(2 * (n - i)):
        print(' ', end='')
    for j in range(i, 0, -1):
        print(j, end='')
    print()

# Q20
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# Q21
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')
    print()

# Q22
n = int(input('Size (max 26): '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(1, i + 1):
        print(chr(64 + j), end='')
    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end='')
    print()

# Q23
n = int(input('Size (max 26): '))
for i in range(n, 0, -1):
    for j in range(i, n + 1):
        print(chr(64 + j), end=' ')
    print()
