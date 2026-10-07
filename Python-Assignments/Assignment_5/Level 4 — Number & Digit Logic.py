
# # LEVEL 4 - CORRECTED SUBMISSION VERSION


# # Q23 - Count Digits
# n = int(input("Enter a positive integer: "))

# temp = n
# digits = 0

# for i in range(1, 20):
#     digits = digits + 1
#     temp = temp // 10

#     if temp == 0:
#         # No break used
#         pass

# print("Digits:", digits)


# # Q24 - Sum of Digits
# n = int(input("Enter an integer: "))

# temp = abs(n)
# total = 0

# for i in range(1, 20):
#     if temp > 0:
#         digit = temp % 10
#         total = total + digit
#         temp = temp // 10

# print("Sum:", total)


# # Q25 - Product of Digits
# n = int(input("Enter an integer: "))

# temp = abs(n)
# product = 1

# for i in range(1, 20):
#     if temp > 0:
#         digit = temp % 10
#         product = product * digit
#         temp = temp // 10

# print("Product:", product)


# # Q26 - Count Even Digits
# n = int(input("Enter an integer: "))

# temp = abs(n)
# count = 0

# for i in range(1, 20):
#     if temp > 0:
#         digit = temp % 10

#         if digit % 2 == 0:
#             count = count + 1

#         temp = temp // 10

# print("Even Digits:", count)


# # Q27 - Sum of Even Digits
# n = int(input("Enter an integer: "))

# temp = abs(n)
# total = 0

# for i in range(1, 20):
#     if temp > 0:
#         digit = temp % 10

#         if digit % 2 == 0:
#             total = total + digit

#         temp = temp // 10

# print("Sum of Even Digits:", total)


# # Q28 - Largest Digit
# n = int(input("Enter an integer: "))

# temp = abs(n)
# largest = 0

# for i in range(1, 20):
#     if temp > 0:
#         digit = temp % 10

#         if digit > largest:
#             largest = digit

#         temp = temp // 10

# print("Largest Digit:", largest)


# # Q29 - Smallest Digit
# n = int(input("Enter an integer: "))

# temp = abs(n)
# smallest = 9

# for i in range(1, 20):
#     if temp > 0:
#         digit = temp % 10

#         if digit < smallest:
#             smallest = digit

#         temp = temp // 10

# print("Smallest Digit:", smallest)


# # Q30 - Reverse a Number
# n = int(input("Enter a positive integer: "))

# temp = n
# reverse = 0

# for i in range(1, 20):
#     if temp > 0:
#         digit = temp % 10
#         reverse = reverse * 10 + digit
#         temp = temp // 10

# print("Reverse:", reverse)


# # Q31 - Palindrome Number
# n = int(input("Enter a number: "))

# original = n
# temp = n
# reverse = 0

# for i in range(1, 20):
#     if temp > 0:
#         digit = temp % 10
#         reverse = reverse * 10 + digit
#         temp = temp // 10

# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# # Q32 - Count a Specific Digit
# n, target = input("Enter number and target digit: ").split()

# n = int(n)
# target = int(target)

# temp = n
# count = 0

# for i in range(1, 20):
#     if temp > 0:
#         digit = temp % 10

#         if digit == target:
#             count = count + 1

#         temp = temp // 10

# print("Count:", count)


# # Q33 - First Digit
# n = int(input("Enter a positive integer: "))

# temp = n

# for i in range(1, 20):
#     if temp >= 10:
#         temp = temp // 10

# print("First Digit:", temp)


# # Q34 - Difference Between Largest and Smallest Digit
# n = int(input("Enter a number: "))

# temp = abs(n)
# largest = 0
# smallest = 9

# for i in range(1, 20):
#     if temp > 0:
#         digit = temp % 10

#         if digit > largest:
#             largest = digit

#         if digit < smallest:
#             smallest = digit

#         temp = temp // 10

# print("Difference:", largest - smallest)


# # Q35 - Digit Position Value
# n = int(input("Enter a positive integer: "))

# temp = n
# position = 1

# for i in range(1, 20):
#     if temp > 0:
#         digit = temp % 10
#         print(digit, position)

#         temp = temp // 10
#         position = position + 1


# # Q36 - Armstrong Number - 3 Digit
# n = int(input("Enter a 3-digit number: "))

# temp = n
# total = 0

# for i in range(3):
#     digit = temp % 10
#     total = total + digit ** 3
#     temp = temp // 10

# if total == n:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")