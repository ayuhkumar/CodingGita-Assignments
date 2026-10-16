# # Type 3: Factorial and Number & Digit Logic

# # Level 1: Basic Digit Logic 

# # Q41
# n = int(input("N: "))
# count = 1 if n == 0 else 0
# temp = n
# while temp > 0:
#     count += 1
#     temp //= 10
# print(count)
# # Output (for N = 58321): 5

# # Q42
# n = int(input("N: "))
# digit_sum = 0
# temp = n
# while temp > 0:
#     digit_sum += temp % 10
#     temp //= 10
# print(digit_sum)
# # Output (for N = 583): 16

# # Q43
# n = int(input("N: "))
# rev = 0
# temp = n
# while temp > 0:
#     rev = rev * 10 + (temp % 10)
#     temp //= 10
# print(rev)
# # Output (for N = 5830): 385

# # Q44
# n = int(input("N: "))
# product = 0 if n == 0 else 1
# temp = n
# while temp > 0:
#     product *= (temp % 10)
#     temp //= 10
# print(product)
# # Output (for N = 234): 24

# # Q45
# n = int(input("N: "))
# temp = n
# while temp > 0:
#     print(temp % 10)
#     temp //= 10
# # Output (for N = 58321):
# # 1
# # 2
# # 3
# # 8
# # 5


# #Level 2: Work with Specific Digits 

# # Q46
# n = int(input("N: "))
# last_digit = n % 10
# first_digit = n
# while first_digit >= 10:
#     first_digit //= 10
# print("First digit:", first_digit)
# print("Last digit:", last_digit)
# # Output (for N = 58321):
# # First digit: 5
# # Last digit: 1

# # Q47
# n = int(input("N: "))
# even_count = 1 if n == 0 else 0
# temp = n
# while temp > 0:
#     d = temp % 10
#     if d % 2 == 0:
#         even_count += 1
#     temp //= 10
# print(even_count)
# # Output (for N = 583204): 4

# # Q48
# n = int(input("N: "))
# odd_count = 0
# temp = n
# while temp > 0:
#     d = temp % 10
#     if d % 2 != 0:
#         odd_count += 1
#     temp //= 10
# print(odd_count)
# # Output (for N = 583204): 2

# # Q49
# n = int(input("N: "))
# even_sum = 0
# temp = n
# while temp > 0:
#     d = temp % 10
#     if d % 2 == 0:
#         even_sum += d
#     temp //= 10
# print(even_sum)
# # Output (for N = 583204): 14

# # Q50
# n = int(input("N: "))
# largest = 0
# temp = n
# while temp > 0:
#     d = temp % 10
#     if d > largest:
#         largest = d
#     temp //= 10
# print(largest)
# # Output (for N = 583204): 8

# # Q51
# n = int(input("N: "))
# smallest = 0 if n == 0 else 9
# temp = n
# while temp > 0:
#     d = temp % 10
#     if d < smallest:
#         smallest = d
#     temp //= 10
# print(smallest)
# # Output (for N = 583204): 0


# #Level 3: Combine Digit Logic

# # Q52
# n = int(input("N: "))
# rev = 0
# temp = n
# while temp > 0:
#     rev = rev * 10 + (temp % 10)
#     temp //= 10
# if rev == n:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
# # Output (for N = 1221): Palindrome

# # Q53
# n = int(input("N: "))
# d = int(input("D: "))
# freq = 1 if (n == 0 and d == 0) else 0
# temp = n
# while temp > 0:
#     if temp % 10 == d:
#         freq += 1
#     temp //= 10
# print(freq)
# # Output (for N = 505250, D = 5): 3

# # Q54
# n = int(input("N: "))
# last_digit = n % 10
# all_same = True
# temp = n // 10
# while temp > 0:
#     if temp % 10 != last_digit:
#         all_same = False
#     temp //= 10
# print("Yes" if all_same else "No")
# # Output (for N = 7777): Yes

# # Q55
# n = int(input("N: "))
# last_digit = n % 10
# temp = n // 10
# middle_sum = 0
# while temp >= 10:
#     middle_sum += temp % 10
#     temp //= 10
# first_digit = temp
# print("First and last digits sum:", first_digit + last_digit)
# print("Middle digits sum:", middle_sum)
# # Output (for N = 58321):
# # First and last digits sum: 6
# # Middle digits sum: 13


# # --- Level 4: Factorial Practice ---

# # Q56
# n = int(input("N: "))
# i = 1
# fact = 1
# while i <= n:
#     fact *= i
#     print(fact)
#     i += 1
# # Output (for N = 5):
# # 1
# # 2
# # 6
# # 24
# # 120

# # Q57
# n = int(input("N: "))
# fact = 1
# i = 1
# while fact < n:
#     i += 1
#     fact *= i
# print("Yes" if fact == n else "No")
# # Output (for N = 24): Yes

# # Q58
# n = int(input("N: "))
# fact = 1
# i = 1
# while (fact * (i + 1)) <= n:
#     i += 1
#     fact *= i
# print(fact)
# # Output (for N = 20): 6