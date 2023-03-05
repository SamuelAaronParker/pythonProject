var = input("Please enter a value: ")
uppercase_var = var.upper()  # changes the input to upper case
print("Uppercase value:", uppercase_var)  # shows the value in upper case
print("Number of characters:", len(var))  # shows the number of characters within the value with "len"
count = 0
for char in var:
    if char.isdecimal():
        count += 1  # adds one the count when its finds a number within the value

if count > 0:
    print("The value contains", count, "numbers")  # displays if there is numbers and how many
else:
    print("The value contains no numbers")  # displays a message to say no numbers contained
