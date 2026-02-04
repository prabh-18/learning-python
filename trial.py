# User input example
user_text = input("Enter a number: ")   # always string
print("You typed (as text):", user_text, "type:", type(user_text))

# Convert text to int
user_number = int(user_text)
double = user_number * 2

print("As a number:", user_number, "type:", type(user_number))
print("Double of your number is:", double)