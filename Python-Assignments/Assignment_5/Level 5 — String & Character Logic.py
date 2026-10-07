
# # LEVEL 5 - STRING & CHARACTER LOGIC


# # Q37 - Print Characters with Index
# text = input("Enter a string: ")

# index = 0

# for character in text:
#     print(index, character)
#     index = index + 1


# # Q38 - Count Characters Without len()
# text = input("Enter a string: ")

# count = 0

# for character in text:
#     count = count + 1

# print("Length:", count)


# # Q39 - Count Vowels and Consonants
# text = input("Enter a string: ")

# vowels = 0
# consonants = 0

# for character in text:
#     if character != " ":
#         if character.lower() in "aeiou":
#             vowels = vowels + 1
#         else:
#             consonants = consonants + 1

# print("Vowels =", vowels)
# print("Consonants =", consonants)


# # Q40 - Character Frequency
# text, target = input("Enter string and target character: ").split()

# count = 0

# for character in text:
#     if character == target:
#         count = count + 1

# print("Count:", count)


# # Q41 - First Occurrence Position
# text, target = input("Enter string and target character: ").split()

# index = 0
# first_position = -1
# found = False

# for character in text:
#     if character == target and found == False:
#         first_position = index
#         found = True

#     index = index + 1

# if first_position == -1:
#     print("Not Found")
# else:
#     print(first_position)


# # Q42 - Count Uppercase and Lowercase
# text = input("Enter a string: ")

# uppercase = 0
# lowercase = 0

# for character in text:
#     if character.isupper():
#         uppercase = uppercase + 1
#     elif character.islower():
#         lowercase = lowercase + 1

# print("Uppercase =", uppercase)
# print("Lowercase =", lowercase)


# # Q43 - Character Code Analyzer
# text = input("Enter a string: ")

# for character in text:
#     print(character, ord(character))


# # Q44 - String Without Vowels
# text = input("Enter a string: ")

# result = ""

# for character in text:
#     if character.lower() not in "aeiou":
#         result = result + character

# print(result)