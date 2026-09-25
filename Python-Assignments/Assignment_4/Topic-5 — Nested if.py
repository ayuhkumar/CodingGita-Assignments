# # Q36

# username, password = input("Enter username and password: ").split()

# if username == "admin":
#     if password == "admin123":
#         print("Login Successful")
#     else:
#         print("Wrong Password")
# else:
#     print("Invalid Username")



# # Q37

# age, test_status = input("Enter age and test status: ").split()

# age = int(age)

# if age >= 18:
#     if test_status == "pass":
#         print("License Approved")
#     else:
#         print("Test Not Passed")
# else:
#     print("Age Not Eligible")



# # Q38

# balance, withdrawal = input("Enter balance and withdrawal amount: ").split()

# balance = int(balance)
# withdrawal = int(withdrawal)

# if withdrawal <= balance:
#     if withdrawal % 100 == 0:
#         print("Withdrawal Successful")
#     else:
#         print("Enter Amount in Multiples of 100")
# else:
#     print("Insufficient Balance")



# # Q39

# marks, attendance = input("Enter marks and attendance: ").split()

# marks = int(marks)
# attendance = int(attendance)

# if attendance >= 75:
#     if marks >= 40:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Not Eligible Due to Attendance")



# # Q40

# account_type, balance = input("Enter account type and balance: ").split()

# balance = int(balance)

# if account_type == "savings":
#     if balance >= 1000:
#         print("Minimum Balance Maintained")
#     else:
#         print("Minimum Balance Not Maintained")
# else:
#     print("Unsupported Account")



# # Q41

# amount, payment_method = input("Enter amount and payment method: ").split()

# amount = int(amount)

# if amount >= 500:
#     if payment_method == "card":
#         print("Card Payment Accepted")
#     elif payment_method == "upi":
#         print("UPI Payment Accepted")
#     else:
#         print("Unsupported Payment Method")
# else:
#     print("Minimum Order Amount Not Reached")



# # Q42

# year, attendance = input("Enter year and attendance: ").split()

# year = int(year)
# attendance = int(attendance)

# if year == 2 or year == 3 or year == 4:
#     if attendance >= 75:
#         print("Room Eligible")
#     else:
#         print("Attendance Too Low")
# else:
#     print("Not Eligible by Year")



# # Q43

# plan, usage = input("Enter plan and usage: ").split()

# usage = int(usage)

# if plan == "basic":
#     if usage > 100:
#         print("Recommend Upgrade")
#     else:
#         print("Basic Plan Is Sufficient")
# else:
#     print("Already on Higher Plan")