# # Type 1: Output Guessing

# # Level 1: Understand the Basic Flow 

# # Q1
# i = 1
# while i <= 4:
#     print(i)
#     i += 1
# # Output:
# # 1
# # 2
# # 3
# # 4

# # Q2
# n = 2
# while n <= 8:
#     print(n, end=" ")
#     n += 2
# # Output: 2 4 6 8 

# # Q3
# x = 5
# while x >= 1:
#     print(x, end=" ")
#     x -= 1
# # Output: 5 4 3 2 1 

# # Q4
# count = 7
# while count < 5:
#     print("Hello")
#     count += 1
# print("Finished")
# # Output: Finished


# #Level 2: Track the Order of Statements 

# # Q5
# i = 1
# while i <= 4:
#     i += 1
#     print(i, end=" ")
# # Output: 2 3 4 5 

# # Q6
# n = 1
# while n <= 3:
#     print(n, end=" ")
#     n += 1
# print("Done")
# # Output: 1 2 3 Done

# # Q7
# x = 1
# while x < 10:
#     print(x, end=" ")
#     x += 2
#     x += 1
# # Output: 1 4 7 

# # Q8
# value = 10
# while value > 0:
#     value -= 3
#     print(value, end=" ")
# # Output: 7 4 1 -2 


# # Level 3: Arithmetic and Accumulation 

# # Q9
# i = 1
# total = 0
# while i <= 4:
#     total += i
#     i += 1
# print(total)
# # Output: 10

# # Q10
# n = 1
# result = 1
# while n <= 4:
#     result *= 2
#     n += 1
# print(result)
# # Output: 16

# # Q11
# n = 11
# while n > 0:
#     print(n % 3, end=" ")
#     n -= 4
# # Output: 2 1 0 

# # Q12
# number = 583
# while number > 0:
#     print(number // 10, end=" ")
#     number //= 10
# # Output: 58 5 0 


# #Level 4: Conditions and Logical Thinking

# # Q13
# i = 1
# while i <= 6:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1
# # Output: 2 4 6 

# # Q14
# n = 1
# while n <= 5:
#     print("Even" if n % 2 == 0 else "Odd", end=" ")
#     n += 1
# # Output: Odd Even Odd Even Odd 

# # Q15
# x = 1
# while x < 10:
#     print(x, end=" ")
#     x *= 2
# # Output: 1 2 4 8 

# # Q16
# i = 5
# while i > 0:
#     print(i, end=" ")
#     i -= 2
# print("Stop:", i)
# # Output: 5 3 1 Stop: -1


# #Level 5: Strings and Tricky Cases

# # Q17
# i = 1
# result = ""
# while i <= 4:
#     result += "A"
#     print(result)
#     i += 1
# # Output:
# # A
# # AA
# # AAA
# # AAAA

# # Q18
# word = "PY"
# while len(word) < 6:
#     print(word)
#     word += "T"
# print(word)
# # Output:
# # PY
# # PYT
# # PYTT
# # PYTTT
# # PYTTTT

# # Q19
# x = 3
# while x > 10:
#     print("Inside")
#     x += 1
# print(x)
# # Output: 3

# # Q20
# # Answer: B. It prints 1 0 -1 -2 ... and continues indefinitely
# # Reasoning: The counter variable `i` starts at 1 and decreases by 1 in each iteration (`i -= 1`).
# # Since `i` keeps becoming smaller, the condition `i <= 4` will always evaluate to True, causing an infinite loop.
