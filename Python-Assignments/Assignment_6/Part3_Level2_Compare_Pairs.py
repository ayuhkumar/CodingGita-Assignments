# Q101
s = input('Number: ')
target = int(input('Target: '))
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if int(s[i]) + int(s[j]) == target:
            print(s[i], s[j])

# Q102
s = input('Number: ')
diff = int(input('D: '))
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if abs(int(s[i]) - int(s[j])) == diff:
            print(s[i], s[j])

# Q103
s = input('Number: ')
for i in range(len(s)):
    first = True
    for k in range(i):
        if s[k] == s[i]:
            first = False
    count = 0
    for j in range(len(s)):
        if s[j] == s[i]:
            count += 1
    if first and count > 1:
        print(s[i])

# Q104
s = input('Number: ')
count = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            count += 1
print(count)

# Q105
a = input('First string: ')
b = input('Second string: ')
for i in range(len(a)):
    first = True
    found = False
    for k in range(i):
        if a[k] == a[i]:
            first = False
    for j in range(len(b)):
        if a[i] == b[j]:
            found = True
    if first and found:
        print(a[i])

# Q106
a = input('First string: ')
b = input('Second string: ')
shared = False
for x in a:
    for y in b:
        if x == y:
            shared = True
print(shared)

# Q107
r = int(input('Rows: '))
seats = int(input('Seats per row: '))
for i in range(1, r + 1):
    print(f'Row {i}:', end=' ')
    for j in range(1, seats + 1):
        print(j, end=' ')
    print()

# Q108
students = int(input('Students: '))
tests = int(input('Tests: '))
class_total = 0
for i in range(1, students + 1):
    total = 0
    for j in range(1, tests + 1):
        total += int(input(f'Student {i}, test {j}: '))
    print(f'Student {i} total: {total}')
    class_total += total
print('Class total:', class_total)

# Q109
days = int(input('Days: '))
stations = int(input('Stations: '))
for i in range(1, days + 1):
    total = 0
    for j in range(1, stations + 1):
        total += float(input(f'Day {i}, station {j}: '))
    print(f'Day {i} total: {total:g}')

# Q110
groups = int(input('Groups: '))
size = int(input('Numbers per group: '))
for i in range(groups):
    largest = float(input('Number: '))
    for j in range(size - 1):
        x = float(input('Number: '))
        if x > largest:
            largest = x
    print(f'{largest:g}')

# Q111
a = int(input('G1 number 1: '))
b = int(input('G1 number 2: '))
c = int(input('G1 number 3: '))
d = int(input('G2 number 1: '))
e = int(input('G2 number 2: '))
f = int(input('G2 number 3: '))
print('Group sums:', a + b + c, d + e + f)
print('Position sums:', a + d, b + e, c + f)

# Q112
n = int(input('N: '))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i + j, end=' ')
    print()

# Q113
n = int(input('Count: '))
zeros = 0
for i in range(n):
    if int(input('Number: ')) == 0:
        zeros += 1
print(zeros)

# Q114
r = int(input('Rows: '))
c = int(input('Columns: '))
for i in range(r):
    for j in range(c):
        print(f'({i}, {j})', end=' ')
    print()

# Q115
text = input('Text: ')
pattern = input('Pattern: ')
for i in range(len(text) - len(pattern) + 1):
    match = True
    for j in range(len(pattern)):
        if text[i + j] != pattern[j]:
            match = False
    if match:
        print(i, end=' ')
print()

# Q116
s = input('String: ')
pairs = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            pairs += 1
print(pairs)

# Q117
a = input('First string: ')
b = input('Second string: ')
same = len(a) == len(b)
for ch in a:
    ca = 0
    cb = 0
    for x in a:
        if x == ch:
            ca += 1
    for x in b:
        if x == ch:
            cb += 1
    if ca != cb:
        same = False
for ch in b:
    found = False
    for x in a:
        if x == ch:
            found = True
    if not found:
        same = False
print(same)

# Q118
s = input('String: ')
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
        print(f'{s[i]}: {count}')

# Q119
s = input('String: ')
i = 0
while i < len(s):
    ch = s[i]
    count = 1
    j = i + 1
    while j < len(s) and s[j] == ch:
        count += 1
        j += 1
    if count >= 2:
        print(f'{ch}: {count}')
    i = j

# Q120
a = input('First string: ')
b = input('Second string: ')
count = 0
for i in range(len(a)):
    if a[i] != b[i]:
        count += 1
print(count)
