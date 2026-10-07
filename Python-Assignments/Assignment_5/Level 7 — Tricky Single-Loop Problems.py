
# # LEVEL 7 - TRICKY SINGLE-LOOP PROBLEMS


# # Q53 - Second Largest Digit
# n = int(input("Enter a number: "))

# temp = n
# largest = -1
# second_largest = -1

# for i in range(1, 20):
#     if temp > 0:
#         digit = temp % 10

#         if digit > largest:
#             second_largest = largest
#             largest = digit
#         elif digit > second_largest and digit != largest:
#             second_largest = digit

#         temp = temp // 10

# print("Second Largest Digit:", second_largest)


# # Q54 - Longest Consecutive Equal Character Run
# text = input("Enter a string: ")

# current_count = 0
# best_count = 0
# previous = ""

# for character in text:
#     if character == previous:
#         current_count = current_count + 1
#     else:
#         current_count = 1
#         previous = character

#     if current_count > best_count:
#         best_count = current_count

# print("Longest Run:", best_count)


# # Q55 - Most Frequent Character - Controlled Approach
# text, target = input("Enter string and target character: ").split()

# count = 0
# total = 0

# for character in text:
#     total = total + 1

#     if character == target:
#         count = count + 1

# frequency = count / total * 100

# print("Count =", count)
# print("Frequency =", round(frequency, 2), "%")


# # Q56 - Running Digit Sum Until the End
# n = int(input("Enter a positive integer: "))

# temp = n
# total = 0

# for i in range(1, 20):
#     if temp > 0:
#         digit = temp % 10
#         total = total + digit
#         print(total)

#         temp = temp // 10


# # Q57 - Number with Most Even Digits
# n = int(input("Enter a positive integer: "))

# temp = n
# even = 0
# odd = 0

# for i in range(1, 20):
#     if temp > 0:
#         digit = temp % 10

#         if digit % 2 == 0:
#             even = even + 1
#         else:
#             odd = odd + 1

#         temp = temp // 10

# if even > odd:
#     print("More Even Digits")
# elif odd > even:
#     print("More Odd Digits")
# else:
#     print("Equal")


# # Q58 - Alternating Digit Sum
# n = int(input("Enter a positive integer: "))

# temp = n
# total = 0
# position = 1

# for i in range(1, 20):
#     if temp > 0:
#         digit = temp % 10

#         if position % 2 == 1:
#             total = total + digit
#         else:
#             total = total - digit

#         position = position + 1
#         temp = temp // 10

# print(total)


# # Q59 - Output Prediction - Accumulator Trap
# total = 0

# for i in range(1, 6):
#     total = total + i * 2
#     print(total)

# # Expected Output:
# # 2
# # 6
# # 12
# # 20
# # 30


# # Q60 - Output Prediction - Condition Inside Loop
# count = 0

# for i in range(1, 11):
#     if i % 2 == 0:
#         count = count + 1

# print(count)

# # Expected Output:
# # 5


# # Q61 - Debug the Accumulator
# total = 0

# for i in range(1, 6):
#     total = total + i

# print(total)

# # Expected Output:
# # 15
# #
# # Mistake in original:
# # sum = i replaces the old value instead of adding to it.