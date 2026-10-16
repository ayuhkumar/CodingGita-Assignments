# Q76
s = input('String: ')
print(len(s))

# Q77
s = input('String: ')
for ch in s:
    print(ch)

# Q78
s = input('String: ')
count = 0
for ch in s:
    if ch.lower() in 'aeiou':
        count += 1
print(count)

# Q79
s = input('String: ')
count = 0
for ch in s:
    if ch.isalpha() and ch.lower() not in 'aeiou':
        count += 1
print(count)

# Q80
print(input('String: ').upper())

# Q81
print(input('String: ').lower())

# Q82
print(input('String: ')[::-1])

# Q83
s = input('String: ')
print(s == s[::-1])

# Q84
s = input('String: ')
count = 0
for ch in s:
    if ch in 'aA':
        count += 1
print(count)

# Q85
s = input('String: ')
result = ''
for ch in s:
    if ch != ' ':
        result += ch
print(result)
