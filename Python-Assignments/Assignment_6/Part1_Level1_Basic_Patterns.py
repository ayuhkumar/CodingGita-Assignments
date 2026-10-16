# Q1
n = int(input('Size: '))
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()

# Q2
rows = int(input('Rows: '))
cols = int(input('Columns: '))
for i in range(rows):
    for j in range(cols):
        print('*', end='')
    print()

# Q3
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()

# Q4
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

# Q5
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(i):
        print(i, end='')
    print()

# Q6
n = int(input('Size (max 26): '))
for i in range(1, n + 1):
    for j in range(i):
        print(chr(64 + i), end='')
    print()

# Q7
n = int(input('Size (max 26): '))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end='')
    print()

# Q8
n = int(input('Size: '))
value = 1
for i in range(1, n + 1):
    for j in range(i):
        print(value, end=' ')
        value += 1
    print()

# Q9
n = int(input('Size: '))
for i in range(1, n + 1):
    for j in range(i):
        print((i + j) % 2, end=' ')
    print()

# Q10
n = int(input('Size: '))
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

# Q11
n = int(input('Size: '))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

# Q12
n = int(input('Size (max 26): '))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(chr(64 + j), end='')
    print()
