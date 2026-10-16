# Q66
n = abs(int(input('Integer: ')))
count = 1
while n >= 10:
    n //= 10
    count += 1
print(count)

# Q67
n = abs(int(input('Integer: ')))
total = 0
for ch in str(n):
    total += int(ch)
print(total)

# Q68
n = abs(int(input('Integer: ')))
product = 1
for ch in str(n):
    product *= int(ch)
print(product)

# Q69
n = abs(int(input('Integer: ')))
print(int(str(n)[::-1]))

# Q70
n = abs(int(input('Integer: ')))
print(str(n) == str(n)[::-1])

# Q71
n = int(input('Integer: '))
prime = n >= 2
for d in range(2, n):
    if n % d == 0:
        prime = False
print(prime)

# Q72
n = int(input('N: '))
for x in range(2, n + 1):
    prime = True
    for d in range(2, x):
        if x % d == 0:
            prime = False
    if prime:
        print(x, end=' ')
print()

# Q73
n = int(input('N: '))
a = 0
b = 1
for i in range(n):
    print(a, end=' ')
    a, b = (b, a + b)
print()

# Q74
a, b = map(int, input('Enter a and b: ').split())
gcd = 1
for d in range(1, min(a, b) + 1):
    if a % d == 0 and b % d == 0:
        gcd = d
print(gcd)

# Q75
a, b = map(int, input('Enter a and b: ').split())
for x in range(max(a, b), a * b + 1):
    if x % a == 0 and x % b == 0:
        print(x)
        break
