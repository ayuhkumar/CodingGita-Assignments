# # LEVEL 2 - COUNTING & ACCUMULATION


# # Q7 - Sum of Numbers in a Range
# start, end = input("Enter start and end: ").split()

# start = int(start)
# end = int(end)

# total = 0

# for i in range(start, end + 1):
#     total = total + i

# print("Sum:", total)


# # Q8 - Count Multiples of 3
# n = int(input("Enter N: "))

# count = 0

# for i in range(1, n + 1):
#     if i % 3 == 0:
#         count = count + 1

# print("Count:", count)


# # Q9 - Sum of Multiples of 4
# n = int(input("Enter N: "))

# total = 0

# for i in range(1, n + 1):
#     if i % 4 == 0:
#         total = total + i

# print("Sum:", total)


# # Q10 - Count Numbers with Two Conditions
# n = int(input("Enter N: "))

# count = 0

# for i in range(1, n + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         count = count + 1

# print("Count:", count)


# # Q11 - Sum Numbers Except Multiples of 3
# n = int(input("Enter N: "))

# total = 0

# for i in range(1, n + 1):
#     if i % 3 != 0:
#         total = total + i

# print("Sum:", total)


# # Q12 - Count Even and Odd Together
# n = int(input("Enter N: "))

# even = 0
# odd = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1

# print("Even =", even)
# print("Odd =", odd)


# # Q13 - Running Sum
# n = int(input("Enter N: "))

# total = 0

# for i in range(1, n + 1):
#     total = total + i
#     print(total)


# # Q14 - Running Product
# n = int(input("Enter N: "))

# product = 1

# for i in range(1, n + 1):
#     product = product * i
#     print(product)