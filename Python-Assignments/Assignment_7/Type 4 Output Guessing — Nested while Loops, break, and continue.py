
# # Type 4: Output Guessing — Nested while Loops, break, and continue


# # Level 1: Understand Nested while Loops 

# # Q59
# i = 1

# while i <= 2:
#     j = 1

#     while j <= 3:
#         print(i, j)
#         j += 1

#     i += 1
# # Output:
# # 1 1
# # 1 2
# # 1 3
# # 2 1
# # 2 2
# # 2 3

# # Q60
# i = 1

# while i <= 3:
#     j = 1

#     while j <= 2:
#         print(j, end=" ")
#         j += 1

#     print()
#     i += 1
# # Output:
# # 1 2 
# # 1 2 
# # 1 2 

# # Q61
# i = 1

# while i <= 3:
#     j = 1

#     while j <= i:
#         print("*", end=" ")
#         j += 1

#     print()
#     i += 1
# # Output:
# # * 
# # * * 
# # * * * 

# # Q62
# i = 1

# while i <= 3:
#     j = i

#     while j <= 3:
#         print(j, end=" ")
#         j += 1

#     print()
#     i += 1
# # Output:
# # 1 2 3 
# # 2 3 
# # 3 

# # Q63
# i = 1

# while i <= 3:
#     j = 1

#     while j <= 2:
#         print(j, end=" ")
#         j += 1

#     print("End")
#     i += 1
# # Output:
# # 1 2 End
# # 1 2 End
# # 1 2 End


# # Level 2: Trace the Flow Carefully

# # Q64
# i = 1

# while i <= 2:
#     j = 1

#     while j <= 2:
#         print(i + j)
#         j += 1

#     i += 1

# print("Finished")
# # Output:
# # 2
# # 3
# # 3
# # 4
# # Finished

# # Q65
# i = 1

# while i <= 2:
#     print("A", i)
#     i += 1

# j = 1

# while j <= 3:
#     print("B", j)
#     j += 1
# # Output:
# # A 1
# # A 2
# # B 1
# # B 2
# # B 3

# # Q66
# i = 1
# j = 1

# while i <= 3:
#     while j <= 2:
#         print(i, j)
#         j += 1

#     i += 1
# # Output:
# # 1 1
# # 1 2

# # Q67
# i = 1

# while i <= 3:
#     j = 1

#     while j <= 2:
#         print(i, end="")
#         j += 1

#     print()
#     i += 2
# # Output:
# # 11
# # 33

# # Q68
# i = 1

# while i <= 3:
#     j = 1

#     while j < i:
#         print(j, end=" ")
#         j += 1

#     print("X")
#     i += 1
# # Output:
# # X
# # 1 X
# # 1 2 X


# #Level 3: Nested Loops with break
# # Q69
# i = 1

# while i <= 3:
#     j = 1

#     while j <= 4:
#         if j == 3:
#             break

#         print(i, j)
#         j += 1

#     i += 1
# # Output:
# # 1 1
# # 1 2
# # 2 1
# # 2 2
# # 3 1
# # 3 2

# # Q70
# i = 1

# while i <= 2:
#     j = 1

#     while j <= 4:
#         print(j, end=" ")

#         if j == 2:
#             break

#         j += 1

#     print("|")
#     i += 1
# # Output:
# # 1 2 |
# # 1 2 |

# # Q71
# i = 1

# while i <= 2:
#     j = 1

#     while j <= 2:
#         if j == 5:
#             break

#         print(i, j)
#         j += 1

#     i += 1
# # Output:
# # 1 1
# # 1 2
# # 2 1
# # 2 2

# # Q72
# i = 1

# while i <= 3:
#     j = 1

#     while j <= 3:
#         if j == 2:
#             break

#         print(i, j)
#         j += 1

#     print("Next row")
#     i += 1
# # Output:
# # 1 1
# # Next row
# # 2 1
# # Next row
# # 3 1
# # Next row


# #  Level 4: Nested Loops with continue 

# # Q73
# i = 1

# while i <= 2:
#     j = 0

#     while j < 4:
#         j += 1

#         if j == 2:
#             continue

#         print(i, j)

#     i += 1
# # Output:
# # 1 1
# # 1 3
# # 1 4
# # 2 1
# # 2 3
# # 2 4

# # Q74
# i = 1

# while i <= 5:
#     i += 1

#     if i == 3:
#         continue

#     print(i, end=" ")
# # Output: 2 4 6 

# # Q75
# i = 1

# while i <= 3:
#     j = 0

#     while j < 3:
#         j += 1

#         if j == 2:
#             continue

#         print(j, end=" ")

#     print("Row")
#     i += 1
# # Output:
# # 1 3 Row
# # 1 3 Row
# # 1 3 Row

# # Q76
# i = 1

# while i <= 3:
#     j = 1

#     while j <= 3:
#         if j == i:
#             j += 1
#             continue

#         print(i, j)
#         j += 1

#     i += 1
# # Output:
# # 1 2
# # 1 3
# # 2 1
# # 2 3
# # 3 1
# # 3 2


# # Level 5: Combine Nested Loops, break, and continue

# # Q77
# i = 1

# while i <= 2:
#     j = 0

#     while j < 5:
#         j += 1

#         if j == 2:
#             continue

#         if j == 4:
#             break

#         print(i, j)

#     i += 1
# # Output:
# # 1 1
# # 1 3
# # 2 1
# # 2 3

# # Q78
# i = 1

# while i <= 3:
#     j = 1

#     while j <= 4:
#         if j == 2:
#             j += 1
#             continue

#         if i == 3 and j == 4:
#             break

#         print(i * j, end=" ")
#         j += 1

#     print("End")
#     i += 1

# print("Done")
# # Output:
# # 1 3 4 End
# # 2 6 8 End
# # 3 9 End
# # Done