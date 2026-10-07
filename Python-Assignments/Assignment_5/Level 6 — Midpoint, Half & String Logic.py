
# # LEVEL 6 - MIDPOINT, HALF & STRING LOGIC

# # Q45 - Find the Middle Character
# text = input("Enter a string: ")

# length = len(text)
# middle = length // 2

# for i in range(length):
#     if i == middle:
#         print(text[i])


# # Q46 - First Half and Second Half
# text = input("Enter an even-length string: ")

# length = len(text)
# middle = length // 2

# first_half = ""
# second_half = ""

# for i in range(length):
#     if i < middle:
#         first_half = first_half + text[i]
#     else:
#         second_half = second_half + text[i]

# print("First Half:", first_half)
# print("Second Half:", second_half)


# # Q47 - Split a String by Length - Odd vs Even
# text = input("Enter a string: ")

# length = len(text)
# middle = length // 2

# first_half = ""
# second_half = ""
# middle_character = ""

# for i in range(length):
#     if length % 2 == 0:
#         if i < middle:
#             first_half = first_half + text[i]
#         else:
#             second_half = second_half + text[i]
#     else:
#         if i < middle:
#             first_half = first_half + text[i]
#         elif i == middle:
#             middle_character = text[i]
#         else:
#             second_half = second_half + text[i]

# if length % 2 == 0:
#     print("First Half:", first_half)
#     print("Second Half:", second_half)
# else:
#     print("First Half:", first_half)
#     print("Middle:", middle_character)
#     print("Second Half:", second_half)


# # Q48 - Compare Two Halves
# text = input("Enter an even-length string: ")

# length = len(text)
# middle = length // 2
# same = True

# for i in range(middle):
#     if text[i] != text[i + middle]:
#         same = False

# if same:
#     print("Equal Halves")
# else:
#     print("Different Halves")


# # Q49 - Mirror the String
# text = input("Enter a string: ")

# length = len(text)
# symmetric = True

# for i in range(length):
#     if text[i] != text[length - 1 - i]:
#         symmetric = False

# if symmetric:
#     print("Symmetric")
# else:
#     print("Not Symmetric")


# # Q50 - Alternate Character Extraction
# text = input("Enter a string: ")

# for i in range(len(text)):
#     if i % 2 == 0:
#         print(text[i], end="")

# print()


# # Q51 - Count Characters at Even and Odd Indexes
# text = input("Enter a string: ")

# even_index = 0
# odd_index = 0

# for i in range(len(text)):
#     if i % 2 == 0:
#         even_index = even_index + 1
#     else:
#         odd_index = odd_index + 1

# print("Even Index =", even_index)
# print("Odd Index =", odd_index)


# # Q52 - Swap Adjacent Characters
# text = input("Enter an even-length string: ")

# result = ""

# for i in range(0, len(text), 2):
#     result = result + text[i + 1] + text[i]

# print(result)