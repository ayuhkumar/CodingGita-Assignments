
# # LEVEL 8 - REAL-LIFE SINGLE-LOOP PROBLEMS


# # Q62 - Daily Expense Analyzer
# n = int(input("Enter number of days: "))

# total = 0
# highest = 0
# lowest = 0

# for i in range(n):
#     expense = float(input("Enter expense: "))

#     total = total + expense

#     if i == 0:
#         highest = expense
#         lowest = expense
#     else:
#         if expense > highest:
#             highest = expense

#         if expense < lowest:
#             lowest = expense

# print("Total:", total)
# print("Highest:", highest)
# print("Lowest:", lowest)


# # Q63 - Student Marks Analyzer
# n = int(input("Enter number of subjects: "))

# total = 0
# highest = 0
# lowest = 0

# for i in range(n):
#     marks = float(input("Enter marks: "))

#     total = total + marks

#     if i == 0:
#         highest = marks
#         lowest = marks
#     else:
#         if marks > highest:
#             highest = marks

#         if marks < lowest:
#             lowest = marks

# average = total / n

# print("Total:", total)
# print("Average:", average)
# print("Highest:", highest)
# print("Lowest:", lowest)


# # Q64 - Attendance Analyzer
# n = int(input("Enter working days: "))

# present = 0
# absent = 0

# for i in range(n):
#     status = input("Enter P or A: ")

#     if status == "P":
#         present = present + 1
#     elif status == "A":
#         absent = absent + 1

# attendance = present / n * 100

# print("Present:", present)
# print("Absent:", absent)
# print("Attendance:", round(attendance, 2), "%")


# # Q65 - Electricity Usage Analyzer
# n = int(input("Enter number of days: "))

# total_units = 0
# days_above_10 = 0

# for i in range(n):
#     units = int(input("Enter units: "))

#     total_units = total_units + units

#     if units > 10:
#         days_above_10 = days_above_10 + 1

# print("Total Units:", total_units)
# print("Days Above 10:", days_above_10)


# # Q66 - Shopping Bill Analyzer
# n = int(input("Enter number of products: "))

# total_bill = 0
# products_above_1000 = 0

# for i in range(n):
#     price = float(input("Enter price: "))

#     total_bill = total_bill + price

#     if price > 1000:
#         products_above_1000 = products_above_1000 + 1

# print("Total Bill:", total_bill)
# print("Products Above 1000:", products_above_1000)


# # Q67 - Login Attempt Analyzer
# n = int(input("Enter number of attempts: "))

# successful = 0
# failed = 0

# for i in range(n):
#     attempt = input("Enter success or failed: ")

#     if attempt == "success":
#         successful = successful + 1
#     elif attempt == "failed":
#         failed = failed + 1

# success_rate = successful / n * 100

# print("Successful:", successful)
# print("Failed:", failed)
# print("Success Rate:", round(success_rate, 2), "%")