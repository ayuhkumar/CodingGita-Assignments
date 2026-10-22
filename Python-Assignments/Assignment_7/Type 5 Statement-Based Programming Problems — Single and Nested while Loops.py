# # Type 5: Statement-Based Programming Problems — Single and Nested while Loops

# # Part A: Single while Loop Problems

# # Q79
# n = int(input("N: "))
# if n <= 1:
#     print("Not Prime")
# else:
#     d = 2
#     is_prime = True
#     while d * d <= n:
#         if n % d == 0:
#             is_prime = False
#             break
#         d += 1
#     if is_prime:
#         print("Prime")
#     else:
#         print("Not Prime")
# # Output (for N = 17): Prime

# # Q80
# a = int(input("A: "))
# b = int(input("B: "))
# while b != 0:
#     temp = b
#     b = a % b
#     a = temp
# print(a)
# # Output (for A = 18, B = 24): 6

# # Q81
# a = int(input("A: "))
# b = int(input("B: "))
# x = a
# y = b
# while y != 0:
#     temp = y
#     y = x % y
#     x = temp
# gcd = x
# lcm = (a * b) // gcd
# print(lcm)
# # Output (for A = 6, B = 8): 24

# # Q82
# n = int(input("N: "))
# div_sum = 0
# d = 1
# while d < n:
#     if n % d == 0:
#         div_sum += d
#     d += 1
# if div_sum == n and n > 1:
#     print("Perfect")
# else:
#     print("Not Perfect")
# # Output (for N = 28): Perfect

# # Q83
# n = int(input("N: "))
# temp = n
# fact_sum = 0
# while temp > 0:
#     digit = temp % 10
#     if digit == 0 or digit == 1:
#         fact = 1
#     elif digit == 2:
#         fact = 2
#     elif digit == 3:
#         fact = 6
#     elif digit == 4:
#         fact = 24
#     elif digit == 5:
#         fact = 120
#     elif digit == 6:
#         fact = 720
#     elif digit == 7:
#         fact = 5040
#     elif digit == 8:
#         fact = 40320
#     else:
#         fact = 362880
#     fact_sum += fact
#     temp //= 10
# if fact_sum == n:
#     print("Strong")
# else:
#     print("Not Strong")
# # Output (for N = 145): Strong

# # Q84
# n = int(input("N: "))
# temp = n
# if n == 0:
#     num_digits = 1
# else:
#     num_digits = 0
# temp_count = n
# while temp_count > 0:
#     num_digits += 1
#     temp_count //= 10

# armstrong_sum = 0
# while temp > 0:
#     digit = temp % 10
#     armstrong_sum += digit ** num_digits
#     temp //= 10
# if armstrong_sum == n:
#     print("Armstrong")
# else:
#     print("Not Armstrong")
# # Output (for N = 153): Armstrong

# # Q85
# n = int(input("N: "))
# binary = 0
# place = 1
# if n == 0:
#     print(0)
# else:
#     while n > 0:
#         rem = n % 2
#         binary += rem * place
#         place *= 10
#         n //= 2
#     print(binary)
# # Output (for N = 13): 1101

# # Q86
# n = int(input("N: "))
# div_sum = 0
# d = 1
# while d <= n:
#     if n % d == 0:
#         div_sum += d
#     d += 1
# print(div_sum)
# # Output (for N = 12): 28


# # Part B: Nested Loops and Statement-Based Problems

# # Q87
# n = int(input("N: "))
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         if j < i:
#             print(j, end=" ")
#         else:
#             print(j, end="")
#         j += 1
#     print()
#     i += 1
# # Output (for N = 4):
# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4

# # Q88
# r = int(input("R: "))
# c = int(input("C: "))
# i = 1
# while i <= r:
#     j = 1
#     while j <= c:
#         if i == 1 or i == r or j == 1 or j == c:
#             if j < c:
#                 print("*", end=" ")
#             else:
#                 print("*", end="")
#         else:
#             if j < c:
#                 print(" ", end=" ")
#             else:
#                 print(" ", end="")
#         j += 1
#     print()
#     i += 1
# # Output (for R = 4, C = 5):
# # * * * * *
# # *       *
# # *       *
# # * * * * *

# # Q89
# n = int(input("N: "))
# i = 1
# while i <= n:
#     spaces = n - i
#     while spaces > 0:
#         print("  ", end="")
#         spaces -= 1
#     j = 1
#     while j <= i:
#         if j < i:
#             print("*", end=" ")
#         else:
#             print("*", end="")
#         j += 1
#     print()
#     i += 1
# # Output (for N = 3):
# #     *
# #   * *
# # * * *

# # Q90
# n = int(input("N: "))
# i = 1
# while i <= n:
#     j = 1
#     while j <= n:
#         if j < n:
#             print(i * j, end=" ")
#         else:
#             print(i * j, end="")
#         j += 1
#     print()
#     i += 1
# # Output (for N = 3):
# # 1 2 3
# # 2 4 6
# # 3 6 9

# # Q91
# n = int(input("N: "))
# a = 0
# b = 1
# while a <= n:
#     print(a, end=" ")
#     nxt = a + b
#     a = b
#     b = nxt
# print()
# # Output (for N = 20): 0 1 1 2 3 5 8 13 

# # Q92
# n = int(input("N: "))
# num = 2
# while num <= n:
#     d = 2
#     is_prime = True
#     while d * d <= num:
#         if num % d == 0:
#             is_prime = False
#             break
#         d += 1
#     if is_prime:
#         print(num, end=" ")
#     num += 1
# print()
# # Output (for N = 15): 2 3 5 7 11 13 

# # Q93
# n = int(input("N: "))
# num = 0
# while num <= n:
#     temp = num
#     if num == 0:
#         num_digits = 1
#     else:
#         num_digits = 0
#     t = num
#     while t > 0:
#         num_digits += 1
#         t //= 10
#     total = 0
#     while temp > 0:
#         digit = temp % 10
#         total += digit ** num_digits
#         temp //= 10
#     if total == num:
#         print(num, end=" ")
#     num += 1
# print()
# # Output (for N = 500): 0 1 2 3 4 5 6 7 8 9 153 370 371 407 

# # Q94
# n = int(input("N: "))
# num = 2
# while num <= n:
#     div_sum = 0
#     d = 1
#     while d < num:
#         if num % d == 0:
#             div_sum += d
#         d += 1
#     if div_sum == num:
#         print(num, end=" ")
#     num += 1
# print()
# # Output (for N = 1000): 6 28 496 

# # Q95
# n = int(input("N: "))
# a = 1
# while a < n - a:
#     b = n - a
#     print(f"{a} + {b}")
#     a += 1
# # Output (for N = 7):
# # 1 + 6
# # 2 + 5
# # 3 + 4

# # Q96
# s = int(input("S: "))
# if 1 <= s <= 18:
#     num = 10
#     while num <= 99:
#         d1 = num // 10
#         d2 = num % 10
#         if d1 + d2 == s:
#             print(num, end=" ")
#         num += 1
#     print()
# # Output (for S = 5): 14 23 32 41 50 

# # Q97
# a = int(input("A: "))
# b = int(input("B: "))
# d = 1
# if a < b:
#     limit = a
# else:
#     limit = b
# while d <= limit:
#     if a % d == 0 and b % d == 0:
#         print(d, end=" ")
#     d += 1
# print()
# # Output (for A = 12, B = 18): 1 2 3 6 

# # Q98
# n = int(input("N: "))
# found = False
# a = 2
# while a * a <= n:
#     if n % a == 0:
#         b = n // a
#         is_prime_a = True
#         d = 2
#         while d * d <= a:
#             if a % d == 0:
#                 is_prime_a = False
#                 break
#             d += 1
#         is_prime_b = True
#         d = 2
#         while d * d <= b:
#             if b % d == 0:
#                 is_prime_b = False
#                 break
#             d += 1
#         if is_prime_a and is_prime_b:
#             print(f"{a} * {b}")
#             found = True
#     a += 1
# if not found:
#     print("No prime factor pair")
# # Output (for N = 15): 3 * 5