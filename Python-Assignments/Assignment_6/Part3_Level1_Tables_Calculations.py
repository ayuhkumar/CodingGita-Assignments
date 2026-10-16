# Q96
n = int(input('N: '))
k = int(input('K: '))
for i in range(1, n + 1):
    for j in range(1, k + 1):
        print(f'{i} x {j} = {i * j}')

# Q97
n = int(input('N: '))
for x in range(1, n + 1):
    print(f'{x}:', end=' ')
    for d in range(1, x + 1):
        if x % d == 0:
            print(d, end=' ')
    print()

# Q98
n = int(input('N: '))
for x in range(1, n + 1):
    count = 0
    for d in range(1, x + 1):
        if x % d == 0:
            count += 1
    print(f'{x}: {count}')

# Q99
n = int(input('N: '))
for x in range(2, n + 1):
    total = 0
    for d in range(1, x):
        if x % d == 0:
            total += d
    if total == x:
        print(x)

# Q100
n = int(input('N: '))
for x in range(2, n + 1):
    prime = True
    for d in range(2, x):
        if x % d == 0:
            prime = False
    if prime:
        print(x, end=' ')
print()
