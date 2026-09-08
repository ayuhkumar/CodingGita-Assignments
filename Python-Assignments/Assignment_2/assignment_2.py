#Topic 1: Type Casting

# Question 1

age = "25"
age = int(age)

print(age)
print(type(age))

# Question 2

marks = "75.5"
marks = float(marks)

print(marks)
print(type(marks))

# Question 3

number = 50
number = float(number)

print(number)
print(type(number))

# Question 4

marks = 85.9
marks = int(marks)

print(marks)
print(type(marks))

# Question 5

roll_number = 101
roll_number = str(roll_number)

print(roll_number)
print(type(roll_number))

# Question 6

age = "18"
marks = "92.5"
number = 100
decimal_number = 45.8

age = int(age)
marks = float(marks)
number = str(number)
decimal_number = int(decimal_number)

print(age, type(age))
print(marks, type(marks))
print(number, type(number))
print(decimal_number, type(decimal_number))

# Question 7

a = "20"
b = int(a)

c = 10.8
d = int(c)

e = 25
f = str(e)

print(b)
print(d)
print(f)
print(type(b))
print(type(d))
print(type(f))

# Question 8

age = "19"
new_age = int(age) + 1

print("Age:", new_age)


# Question 9

marks = "85"
marks = int(marks)

final_marks = marks + 5

print("Final Marks:", final_marks)


# Question 10

price = "1499.50"
price = float(price)

delivery_charges = 99.50
total_amount = price + delivery_charges

print("Total Amount:", total_amount)





#Topic 2: Arithmetic Operators

# Question 11

a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

# Question 12

a = 17
b = 5

print(a / b)
print(a // b)
print(a % b)

# Question 13

result = 10 + 5 * 2
print(result)

result = (10 + 5) * 2
print(result)

# Question 14

result = 20 - 4 * 3 + 2
print(result)

result = 20 - (4 * 3) + 2
print(result)


# Question 15

print(2 ** 3)
print(3 ** 2)
print(10 ** 2)

side = 5
area = side ** 2

print("Area of Square:", area)


# Question 16

notebook = 80
pen = 20
pencil = 10

total_amount = notebook + pen + pencil

print("Total Amount:", total_amount)


# Question 17

notebook_cost = 3 * 50
pen_cost = 2 * 15
calculator_cost = 1 * 500

total_bill = notebook_cost + pen_cost + calculator_cost

print("Notebook Cost:", notebook_cost)
print("Pen Cost:", pen_cost)
print("Calculator Cost:", calculator_cost)
print("Total Bill:", total_bill)


# Question 18

students = 47
group_size = 5

complete_groups = students // group_size
students_left = students % group_size

print("Complete Groups:", complete_groups)
print("Students Left:", students_left)


# Question 19

python_marks = 85
math_marks = 78
physics_marks = 92

total_marks = python_marks + math_marks + physics_marks
average_marks = total_marks / 3

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)


# Question 20

english = 78
mathematics = 85
python_marks = 92
physics = 81
chemistry = 74

total_marks = english + mathematics + python_marks + physics + chemistry
percentage = total_marks / 5

print("Total Marks:", total_marks)
print("Percentage:", percentage)




#Topic 3: Digit Extraction


# Question 21

number = 583

ones_digit = number % 10

print("Ones Digit:", ones_digit)

# Question 22

number = 583

tens_digit = (number // 10) % 10

print("Tens Digit:", tens_digit)

# Question 22

number = 583

tens_digit = (number // 10) % 10

print("Tens Digit:", tens_digit)


# Question 24

number = 746

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100

print("Ones Digit:", ones_digit)
print("Tens Digit:", tens_digit)
print("Hundreds Digit:", hundreds_digit)

# Question 25

number = 5829

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 10
thousands_digit = number // 1000

print("Ones Digit:", ones_digit)
print("Tens Digit:", tens_digit)
print("Hundreds Digit:", hundreds_digit)
print("Thousands Digit:", thousands_digit)

# Question 26

number = 583

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100

sum_of_digits = ones_digit + tens_digit + hundreds_digit

print("Sum of Digits:", sum_of_digits)


# Question 27

number = 4726

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 10
thousands_digit = number // 1000

sum_of_digits = ones_digit + tens_digit + hundreds_digit + thousands_digit

print("Sum of Digits:", sum_of_digits)


# Question 28

number = 234

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100

product_of_digits = ones_digit * tens_digit * hundreds_digit

print("Product of Digits:", product_of_digits)

# Question 29

number = 583

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100

reversed_number = ones_digit * 100 + tens_digit * 10 + hundreds_digit

print("Original Number:", number)
print("Reversed Number:", reversed_number)

# Question 30

number = 4726

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 10
thousands_digit = number // 1000

reversed_number = ones_digit * 1000 + tens_digit * 100 + hundreds_digit * 10 + thousands_digit

print("Original Number:", number)
print("Reversed Number:", reversed_number)


# Question 31

number = 5834

thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
ones_digit = number % 10

print("Thousands Place:", thousands_digit * 1000)
print("Hundreds Place:", hundreds_digit * 100)
print("Tens Place:", tens_digit * 10)
print("Ones Place:", ones_digit)


# Question 32

number = 583

hundreds_digit = number // 100
ones_digit = number % 10

difference = hundreds_digit - ones_digit

print("Difference:", difference)


# Question 33

number = 583
ones = number % 10

print("Ones Digit:", ones)


# Question 34

number = 9365

thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
ones_digit = number % 10

print("Thousands Digit:", thousands_digit)
print("Hundreds Digit:", hundreds_digit)
print("Tens Digit:", tens_digit)
print("Ones Digit:", ones_digit)


# Question 35

hundreds = 5
tens = 8
ones = 3

number = hundreds * 100 + tens * 10 + ones

print("Number:", number)






#Topic 4: Real-Life Arithmetic Problems

# Question 36

principal = 10000
rate = 5
time = 2

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)

# Question 37

length = 15
width = 8

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)

# Question 38

radius = 7
pi = 3.14

area = pi * radius ** 2

print("Area:", area)

# Question 39

celsius = 35

fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit:", fahrenheit)

# Question 40

total_seconds = 367

minutes = total_seconds // 60
seconds = total_seconds % 60

print("Minutes:", minutes)
print("Seconds:", seconds)

# Question 40

total_seconds = 367

minutes = total_seconds // 60
seconds = total_seconds % 60

print("Minutes:", minutes)
print("Seconds:", seconds)

# Question 42

basic_salary = 25000
hra = 5000
travel_allowance = 2500
tax_deduction = 3000

gross_salary = basic_salary + hra + travel_allowance
net_salary = gross_salary - tax_deduction

print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)

# Question 43

distance = 120
mileage = 20
fuel_price = 100

fuel_required = distance / mileage
total_fuel_cost = fuel_required * fuel_price

print("Fuel Required:", fuel_required)
print("Total Fuel Cost:", total_fuel_cost)

# Question 44

price = "2500"
discount = "10"

price = float(price)
discount = float(discount)

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount Amount:", discount_amount)
print("Final Price:", final_price)





#Topic 5: Type Casting + Arithmetic Operators

# Question 45

price = "1200"
quantity = "4"

price = int(price)
quantity = int(quantity)

total_price = price * quantity

print("Price:", price)
print("Quantity:", quantity)
print("Total Price:", total_price)

# Question 46

python_marks = "85"
math_marks = "78"
physics_marks = "91"

python_marks = int(python_marks)
math_marks = int(math_marks)
physics_marks = int(physics_marks)

total_marks = python_marks + math_marks + physics_marks
average_marks = total_marks / 3

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

# Question 47

price = "1500"
quantity = "2"
tax_rate = "5"

price = float(price)
quantity = int(quantity)
tax_rate = float(tax_rate)

subtotal = price * quantity
tax_amount = subtotal * tax_rate / 100
final_bill = subtotal + tax_amount

print("Subtotal:", subtotal)
print("Tax Amount:", tax_amount)
print("Final Bill:", final_bill)

# Question 48

price = 2000
discount = 15
gst = 18

discount_amount = price * discount / 100
price_after_discount = price - discount_amount
gst_amount = price_after_discount * gst / 100
final_price = price_after_discount + gst_amount

print("Discount Amount:", discount_amount)
print("Price After Discount:", price_after_discount)
print("GST Amount:", gst_amount)
print("Final Price:", final_price)

# Question 49

price = "500"
quantity = 3

price = int(price)
total = price * quantity

print("Total:", total)

# Question 50

marks1 = "80"
marks2 = "75"
marks3 = "90"

marks1 = int(marks1)
marks2 = int(marks2)
marks3 = int(marks3)

total = marks1 + marks2 + marks3

print("Total Marks:", total)




#Topic 6: Output Prediction


# Question 51

a = "50"
b = int(a)

print(a)
print(b)
print(type(a))
print(type(b))

# Question 52

number = 99.99
result = int(number)

print(number)
print(result)

# Question 53

a = 12
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)


# Question 54

print(10 + 5 * 2)
print((10 + 5) * 2)
print(20 / 5 + 3)
print(20 / (5 + 3))


# Question 55

number = 684

a = number % 10
b = number // 10
c = b % 10
d = number // 100

print(a)
print(c)
print(d)




#Topic 7: Mixed Debugging

# Question 56

student_name = "Ravi"
marks = "85"

marks = int(marks)
total = marks + 5

print("Student:", student_name)
print("Marks:", total)
print("Type:", type(total))

# Question 57

number = 746

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

print("Ones:", ones)
print("Tens:", tens)
print("Hundreds:", hundreds)


# Question 58

price = "2000"
discount = "15"

price = float(price)
discount = float(discount)

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount:", discount_amount)
print("Final Price:", final_price)



# Question 59

student_name = "Rahul"
marks1 = "85"
marks2 = "90"
marks3 = "78"

marks1 = int(marks1)
marks2 = int(marks2)
marks3 = int(marks3)

total = marks1 + marks2 + marks3
average = total / 3

print("Student:", student_name)
print("Total Marks:", total)
print("Average:", average)
print("Marks Type:", type(total))



# Question 60

# Part A - Number Analysis

number = 5836

thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
ones_digit = number % 10

sum_of_digits = thousands_digit + hundreds_digit + tens_digit + ones_digit

reversed_number = ones_digit * 1000 + tens_digit * 100 + hundreds_digit * 10 + thousands_digit

print("Thousands Digit:", thousands_digit)
print("Hundreds Digit:", hundreds_digit)
print("Tens Digit:", tens_digit)
print("Ones Digit:", ones_digit)
print("Sum of Digits:", sum_of_digits)
print("Reversed Number:", reversed_number)


# Part B - Product Billing

price = "1250"
quantity = "4"
discount = "10"

price = float(price)
quantity = int(quantity)
discount = float(discount)

subtotal = price * quantity
discount_amount = subtotal * discount / 100
final_amount = subtotal - discount_amount

print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)







