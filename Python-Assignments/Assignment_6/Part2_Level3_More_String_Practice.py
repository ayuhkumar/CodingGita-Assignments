# Q86
s = input('Sentence: ')
count = 0
in_word = False
for ch in s:
    if ch != ' ' and (not in_word):
        count += 1
        in_word = True
    elif ch == ' ':
        in_word = False
print(count)

# Q87
s = input('String: ')
result = ''
for ch in s:
    if ch == 'a':
        result += 'e'
    else:
        result += ch
print(result)

# Q88
s = input('String: ')
ch = input('Character: ')
print(ch in s)

# Q89
a = input('First string: ')
b = input('Second string: ')
print(a == b)

# Q90
s = input('String: ')
count = 0
for ch in s:
    if ch >= '0' and ch <= '9':
        count += 1
print(count)

# Q91
s = input('String: ')
count = 0
for ch in s:
    if ch.isalpha() and ch.isupper():
        count += 1
print(count)

# Q92
s = input('String: ')
count = 0
for ch in s:
    if ch.isalpha() and ch.islower():
        count += 1
print(count)

# Q93
s = input('String: ')
result = ''
for ch in s:
    if ch.lower() not in 'aeiou':
        result += ch
print(result)

# Q94
s = input('String: ')
result = ''
for ch in s:
    if not '0' <= ch <= '9':
        result += ch
print(result)

# Q95
s = input('String: ')
result = ''
for ch in s:
    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch
print(result)
