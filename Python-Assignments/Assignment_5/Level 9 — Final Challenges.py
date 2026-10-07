
# # LEVEL 9 - FINAL CHALLENGES


# # Q68 - Number Profile
# n = int(input("Enter a positive integer: "))

# temp = n

# digits = 0
# total = 0
# largest = 0
# smallest = 9
# even_digits = 0
# odd_digits = 0

# for i in range(1, 20):
#     if temp > 0:
#         digit = temp % 10

#         digits = digits + 1
#         total = total + digit

#         if digit > largest:
#             largest = digit

#         if digit < smallest:
#             smallest = digit

#         if digit % 2 == 0:
#             even_digits = even_digits + 1
#         else:
#             odd_digits = odd_digits + 1

#         temp = temp // 10

# print("Digits:", digits)
# print("Sum:", total)
# print("Largest:", largest)
# print("Smallest:", smallest)
# print("Even Digits:", even_digits)
# print("Odd Digits:", odd_digits)


# # Q69 - String Balance Challenge
# text = input("Enter a string: ")

# total_characters = 0
# vowels = 0
# consonants = 0
# uppercase = 0
# lowercase = 0
# even_index_characters = 0

# for i in range(len(text)):
#     character = text[i]

#     total_characters = total_characters + 1

#     if i % 2 == 0:
#         even_index_characters = even_index_characters + 1

#     if character != " ":
#         if character.lower() in "aeiou":
#             vowels = vowels + 1
#         else:
#             consonants = consonants + 1

#         if character.isupper():
#             uppercase = uppercase + 1
#         elif character.islower():
#             lowercase = lowercase + 1

# print("Total Characters:", total_characters)
# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Uppercase:", uppercase)
# print("Lowercase:", lowercase)
# print("Even Index Characters:", even_index_characters)