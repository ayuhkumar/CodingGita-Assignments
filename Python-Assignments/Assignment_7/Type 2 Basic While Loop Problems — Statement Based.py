# # Type 2: Basic While Loop Problems — Statement Based

# # Level 1: Basic Counting

# # Q21
# n = int(input("N: "))
# i = 1
# while i <= n:
#     print(i)
#     i += 1
# # Output (for N = 5):
# # 1
# # 2
# # 3
# # 4
# # 5

# # Q22
# n = int(input("N: "))
# while n >= 1:
#     print(n)
#     n -= 1
# # Output (for N = 5):
# # 5
# # 4
# # 3
# # 2
# # 1

# # Q23
# n = int(input("N: "))
# i = 2
# while i <= n:
#     print(i)
#     i += 2
# # Output (for N = 10):
# # 2
# # 4
# # 6
# # 8
# # 10

# # Q24
# n = int(input("N: "))
# i = 1
# while i <= n:
#     print(i)
#     i += 2
# # Output (for N = 9):
# # 1
# # 3
# # 5
# # 7
# # 9

# # Q25
# k = int(input("K: "))
# n = int(input("N: "))
# val = k
# while val <= n:
#     print(val)
#     val += k
# # Output (for K = 3, N = 15):
# # 3
# # 6
# # 9
# # 12
# # 15


# # Level 2: Counting with Small Changes

# # Q26
# n = int(input("N: "))
# i = 1
# while i <= 10:
#     print(f"{n} x {i} = {n * i}")
#     i += 1
# # Output (for N = 4):
# # 4 x 1 = 4
# # 4 x 2 = 8
# # 4 x 3 = 12
# # 4 x 4 = 16
# # 4 x 5 = 20
# # 4 x 6 = 24
# # 4 x 7 = 28
# # 4 x 8 = 32
# # 4 x 9 = 36
# # 4 x 10 = 40

# # Q27
# start = int(input("START: "))
# step = int(input("STEP: "))
# count = 0
# val = start
# while count < 5:
#     print(val)
#     val += step
#     count += 1
# # Output (for START = 2, STEP = 3):
# # 2
# # 5
# # 8
# # 11
# # 14

# # Q28
# n = int(input("N: "))
# total = 0
# i = 1
# while i <= n:
#     total += i
#     i += 1
# print(total)
# # Output (for N = 5): 15

# # Q29
# n = int(input("N: "))
# total = 0
# i = 2
# while i <= n:
#     total += i
#     i += 2
# print(total)
# # Output (for N = 10): 30

# # Q30
# n = int(input("N: "))
# total = 0
# i = 1
# while i <= n:
#     total += i
#     i += 2
# print(total)
# # Output (for N = 7): 16


# #Level 3: Simple Repeated Calculations

# # Q31
# price = int(input("PRICE: "))
# quantity = int(input("QUANTITY: "))
# total_cost = 0
# i = 0
# while i < quantity:
#     total_cost += price
#     i += 1
# print(total_cost)
# # Output (for PRICE = 20, QUANTITY = 4): 80

# # Q32
# daily_saving = int(input("DAILY_SAVING: "))
# days = int(input("DAYS: "))
# total_savings = 0
# i = 0
# while i < days:
#     total_savings += daily_saving
#     i += 1
# print(total_savings)
# # Output (for DAILY_SAVING = 25, DAYS = 6): 150

# # Q33
# base = int(input("BASE: "))
# power = int(input("POWER: "))
# result = 1
# i = 0
# while i < power:
#     result *= base
#     i += 1
# print(result)
# # Output (for BASE = 3, POWER = 4): 81

# # Q34
# n = int(input("N: "))
# factorial = 1
# i = 1
# while i <= n:
#     factorial *= i
#     i += 1
# print(factorial)
# # Output (for N = 5): 120

# # Q35
# start = int(input("START: "))
# end = int(input("END: "))
# total = 0
# i = start
# while i <= end:
#     total += i
#     i += 1
# print(total)
# # Output (for START = 3, END = 7): 25


# # Level 4: Read the Condition Carefully

# # Q36
# n = int(input("N: "))
# while n >= 2:
#     print(n)
#     n -= 2
# # Output (for N = 10):
# # 10
# # 8
# # 6
# # 4
# # 2

# # Q37
# n = int(input("N: "))
# while n > 0:
#     n //= 2
#     print(n)
# # Output (for N = 20):
# # 10
# # 5
# # 2
# # 1
# # 0

# # Q38
# n = int(input("N: "))
# steps = 0
# while n > 0:
#     n -= 3
#     steps += 1
# print(steps)
# # Output (for N = 11): 4

# # Q39
# saved = int(input("SAVED: "))
# daily_amount = int(input("DAILY_AMOUNT: "))
# target = int(input("TARGET: "))
# days = 0
# while saved < target:
#     saved += daily_amount
#     days += 1
# print(days)
# # Output (for SAVED = 20, DAILY_AMOUNT = 15, TARGET = 70): 4

# # Q40
# start = int(input("START: "))
# step = int(input("STEP: "))
# while start >= 0:
#     print(start)
#     start -= step
# # Output (for START = 20, STEP = 5):
# # 20
# # 15
# # 10
# # 5
# # 0
