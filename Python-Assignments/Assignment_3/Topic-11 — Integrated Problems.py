# Q60

student_name = input("Enter student name: ")

python_marks, math_marks, physics_marks = input("Enter three marks: ").split()

python_marks = int(python_marks)
math_marks = int(math_marks)
physics_marks = int(physics_marks)

total = python_marks + math_marks + physics_marks
average = total / 3

print(f"Name: {student_name}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")

# Q61

student_id = input("Enter student ID: ")

parts = student_id.split("-")

degree = parts[0]
batch = parts[1]
branch = parts[2]
roll_number = int(parts[3])

last_three = student_id[-3:]

print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll Number: {roll_number}")
print(f"Last Three Characters: {last_three}")

# Q62

full_name = input("Enter full name: ")

name_parts = full_name.split()

first_name = name_parts[0]
last_name = name_parts[2]

username = first_name.lower() + "." + last_name.lower()

print(username)

# Q63

sentence = input("Enter a sentence: ")

words = sentence.split()

first_word = words[0]
last_word = words[-1]

print("First word:", first_word)
print("Last word:", last_word)
print("Number of words:", len(words))

# Q64

email = input("Enter email: ")

print("@ Present:", "@" in email)

email_parts = email.split("@")

username = email_parts[0]
domain = email_parts[1]

print("Username:", username)
print("Domain:", domain)

# Q65

character = input("Enter one character: ")

code = ord(character)
previous_character = chr(code - 1)
next_character = chr(code + 1)

print("Character:", character)
print("Code:", code)
print("Previous:", previous_character)
print("Next:", next_character)

# Q66

product_name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount percentage: "))

subtotal = price * quantity
discount_amount = subtotal * discount / 100
final_total = subtotal - discount_amount

print(f"Product: {product_name}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount_amount:.2f}")
print(f"Final Total: {final_total:.2f}")

# Q67

date = input("Enter date: ")

date_parts = date.split("-")

day = date_parts[0]
month = date_parts[1]
year = date_parts[2]

year_from_slice = date[-4:]

print("Day:", day)
print("Month:", month)
print("Year:", year)
print("Year using slicing:", year_from_slice)

# Q68

text = input("Enter a string: ")

words = text.split()

first_word = words[0]
second_word = words[1]

print("First Word:", first_word)
print("Second Word:", second_word)
print("First Word Reversed:", first_word[::-1])
print("Second Word Reversed:", second_word[::-1])

# Q69

student_code = input("Enter student code: ")

parts = student_code.split("-")

degree = parts[0]
batch = parts[1]
branch = parts[2]
roll = parts[3]

formatted_code = f"{degree}/{branch}/{roll}"

print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll: {roll}")
print(f"Code: {formatted_code}")

# Q70

full_name = input("Enter full name: ")

name_parts = full_name.split()

first_name = name_parts[0]
last_name = name_parts[-1]

first_name_part = first_name[:3].upper()
last_name_part = last_name[1:4].lower()
reversed_name = full_name[::-1]

print(f"Original: {full_name}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"First Name (Upper Part): {first_name_part}")
print(f"Last Name (Lower Part): {last_name_part}")
print(f"Full Name Reversed: {reversed_name}")

