# # Q58

# student_id = input("Enter student ID: ")

# parts = student_id.split("-")

# degree = parts[0]
# batch = parts[1]
# branch = parts[2]
# roll_number = parts[3]

# if branch == "CSE":
#     print("CSE Student")
# else:
#     print("Non-CSE Student")



# # Q59

# email = input("Enter email: ")

# parts = email.split("@")
# domain = parts[1]

# if domain == "gmail.com":
#     print("Gmail User")
# else:
#     print("Other Email Provider")



# # Q60

# full_name = input("Enter full name: ")

# parts = full_name.split()

# first_name = parts[0]
# last_name = parts[-1]

# username = first_name.lower() + "." + last_name.lower()

# if "." in username:
#     print("Valid Username Format")
# else:
#     print("Invalid Username Format")



# # Q61

# number = int(input("Enter a positive integer: "))

# if number < 10:
#     print("One Digit")
# elif number < 100:
#     print("Two Digits")
# elif number < 1000:
#     print("Three Digits")
# else:
#     print("Four or More Digits")



# # Q62

# price, quantity = input("Enter price and quantity: ").split()

# price = float(price)
# quantity = int(quantity)

# subtotal = price * quantity

# if subtotal >= 5000:
#     discount_percentage = 20
# elif subtotal >= 2000:
#     discount_percentage = 10
# else:
#     discount_percentage = 0

# discount_amount = subtotal * discount_percentage / 100
# final_amount = subtotal - discount_amount

# print(f"Subtotal: {subtotal:.0f}")
# print(f"Discount: {discount_percentage}%")
# print(f"Final: {final_amount:.2f}")



# # Q63

# units = int(input("Enter units consumed: "))

# if units <= 100:
#     rate = 5
# elif units <= 300:
#     rate = 7
# else:
#     rate = 10

# bill = units * rate

# print(f"Units: {units}")
# print(f"Rate: ₹{rate}")
# print(f"Bill: ₹{bill}")



# # Q64

# print("1. Check Balance")
# print("2. Deposit")
# print("3. Withdraw")
# print("4. Exit")

# choice = int(input("Enter choice: "))

# balance = 10000

# match choice:
#     case 1:
#         print(f"Balance: {balance}")

#     case 2:
#         deposit = int(input("Enter deposit amount: "))
#         balance += deposit
#         print("Deposit Successful")
#         print(f"Balance: {balance}")

#     case 3:
#         withdrawal = int(input("Enter withdrawal amount: "))

#         if withdrawal <= balance:
#             balance -= withdrawal
#             print("Withdrawal Successful")
#             print(f"Balance: {balance}")
#         else:
#             print("Insufficient Balance")

#     case 4:
#         print("Exit")

#     case _:
#         print("Invalid Choice")



# # Q65

# print("1. Pizza - ₹250")
# print("2. Burger - ₹150")
# print("3. Pasta - ₹200")
# print("4. Sandwich - ₹120")

# choice = int(input("Enter choice: "))
# quantity = int(input("Enter quantity: "))

# match choice:
#     case 1:
#         product = "Pizza"
#         price = 250
#     case 2:
#         product = "Burger"
#         price = 150
#     case 3:
#         product = "Pasta"
#         price = 200
#     case 4:
#         product = "Sandwich"
#         price = 120
#     case _:
#         product = ""
#         price = 0

# if price == 0:
#     print("Invalid Choice")
# else:
#     total = price * quantity

#     if total >= 500:
#         discount = total * 10 / 100
#     else:
#         discount = 0

#     final_amount = total - discount

#     print(f"Total: {total}")
#     print(f"Discount: {discount:.2f}")
#     print(f"Final: {final_amount:.2f}")



# # Q66

# python_marks, math_marks, physics_marks, attendance = input(
#     "Enter three marks and attendance: "
# ).split()

# python_marks = int(python_marks)
# math_marks = int(math_marks)
# physics_marks = int(physics_marks)
# attendance = int(attendance)

# total = python_marks + math_marks + physics_marks
# average = total / 3

# if attendance >= 75:
#     if average >= 90:
#         print("Outstanding")
#     elif average >= 75:
#         print("Very Good")
#     elif average >= 60:
#         print("Good")
#     elif average >= 40:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Not Eligible")



# # Q67

# distance, ride_type = input("Enter distance and ride type: ").split()

# distance = float(distance)

# match ride_type:
#     case "normal":
#         rate = 15
#     case "premium":
#         rate = 25
#     case _:
#         rate = 0

# if rate == 0:
#     print("Invalid Ride Type")
# else:
#     fare = distance * rate

#     if distance > 20:
#         fare = fare + (fare * 10 / 100)

#     print(f"Fare: {fare:.2f}")



# # Q68

# score, percentage, category = input(
#     "Enter score, percentage and category: "
# ).split()

# score = int(score)
# percentage = float(percentage)

# match category:
#     case "general":
#         if score >= 80 and percentage >= 75:
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")

#     case "obc":
#         if score >= 70 and percentage >= 70:
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")

#     case "sc":
#         if score >= 60 and percentage >= 60:
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")

#     case _:
#         print("Invalid Category")