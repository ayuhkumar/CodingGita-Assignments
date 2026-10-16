# Q121
n = int(input('N: '))
for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        for c in range(b + 1, n + 1):
            if a * a + b * b == c * c:
                print(a, b, c)

# Q122
n = int(input('N: '))
for x in range(2, n + 1):
    total = 0
    for d in range(1, x):
        if x % d == 0:
            total += d
    if total == x:
        print(x)

# Q123
n = int(input('N: '))
for i in range(1, n + 1):
    for j in range(i, n + 1):
        product = i * j
        seen = False
        for a in range(1, n + 1):
            for b in range(a, n + 1):
                if (a < i or (a == i and b < j)) and a * b == product:
                    seen = True
        if not seen:
            print(product, end=' ')
print()

# Q124
n = int(input('Even N > 2: '))
for a in range(2, n // 2 + 1):
    b = n - a
    pa = True
    pb = True
    for d in range(2, a):
        if a % d == 0:
            pa = False
    for d in range(2, b):
        if b % d == 0:
            pb = False
    if pa and pb:
        print(a, b)

# Q125
n = int(input('Odd N: '))
row_sums = ''
for i in range(1, n + 1):
    total = 0
    for j in range(1, n + 1):
        value = i + j
        print(value, end=' ')
        total += value
    print()
    row_sums += str(total) + ' '
print('Row sums:', row_sums.strip())

# Q126
n = int(input('Number count: '))
previous = None
current = None
peaks = 0
for i in range(n):
    following = int(input('Number: '))
    if previous is not None and current is not None:
        if current > previous and current > following:
            peaks += 1
    previous, current = (current, following)
print(peaks)

# Q127
s = input('Number: ')
repeated = False
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        for k in range(len(s)):
            for m in range(k + 1, len(s)):
                if (i, j) != (k, m) and int(s[i]) + int(s[j]) == int(s[k]) + int(s[m]):
                    repeated = True
if repeated:
    print('Repeated pair sums exist')
else:
    print('No repeated pair sums')

# Q128
n = int(input('N: '))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(abs(i - j), end=' ')
    print()

# Q129
s = input('Number: ')
count = 0
for i in range(1, len(s) - 1):
    if s[i] > s[i - 1] and s[i] > s[i + 1]:
        count += 1
print(count)

# Q130
s = input('Number: ')
count = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] < s[j]:
            count += 1
print(count)

# Q131
s = input('String: ')
result = ''
for i in range(len(s)):
    first = True
    for k in range(i):
        if s[k] == s[i]:
            first = False
    if first:
        count = 0
        for j in range(len(s)):
            if s[j] == s[i]:
                count += 1
        result += s[i] + str(count)
print(result)
