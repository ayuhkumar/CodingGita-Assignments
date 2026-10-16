# Q24
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()
for i in range(n - 1, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

# Q25
n = int(input('Size: '))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
for i in range(2, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

# Q26
n = int(input('Size (max 26): '))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(chr(64 + j), end='')
    print()
for i in range(2, n + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end='')
    print()

# Q27
n = int(input('Size: '))
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print('*', end='')
        else:
            print('#', end='')
    print()

# Q28
n = int(input('Size: '))
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(1, end='')
        else:
            print(0, end='')
    print()

# Q29
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=' ')
    print()

# Q30
n = int(input('Size: '))
for i in range(1, n + 1):
    if i % 2:
        for j in range(1, i + 1):
            print(j, end='')
    else:
        for j in range(i, 0, -1):
            print(j, end='')
    print()

# Q31
n = int(input('Half-height: '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')
    print()

# Q32
n = int(input('Inner number: '))
size = 2 * n - 1
for i in range(size):
    for j in range(size):
        d = min(i, j, size - 1 - i, size - 1 - j)
        print(n - d, end=' ')
    print()
