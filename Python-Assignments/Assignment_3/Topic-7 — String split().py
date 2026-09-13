# Q33

text = "Python is easy"

print(text.split())

# Q34

data = "apple,banana,mango"

print(data.split(","))

# Q35

text = "Python is easy"

print(text.split(","))

# Q36

full_name = input("Enter full name: ")

name_parts = full_name.split()

print(name_parts[0])
print(name_parts[1])
print(name_parts[2])

# Q37

first_name, last_name = input("Enter first and last name: ").split()

print("First Name:", first_name)
print("Last Name:", last_name)

# Q38

a, b, c = input("Enter three numbers: ").split()

a = int(a)
b = int(b)
c = int(c)

total = a + b + c

print("Sum:", total)

# Q39

data = input("Enter student record: ")

student_data = data.split(",")

name = student_data[0]
age = student_data[1]
course = student_data[2]
city = student_data[3]

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("City:", city)


# Q40

email = input("Enter email: ")

email_parts = email.split("@")

username = email_parts[0]
domain = email_parts[1]

print("Username:", username)
print("Domain:", domain)


# Q41

sentence = input("Enter a sentence: ")

words = sentence.split()

print("First word:", words[0])
print("Last word:", words[-1])
print("Total words:", len(words))


