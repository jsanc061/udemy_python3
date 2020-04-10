# using input() to get user input
text = 'First Line.'
text += '\n Second Line. '
message = input(text)
print(message)

info = "This prompt displays your age.\n"
info += 'Enter your age: '
prompt=input(info)
print("Your age is " + prompt)

# numerical user input with int()
age=input("Enter your age: ")
age=int(age)
print(age>21)

age=input("Enter your age:")
age=int(age)
if age>=18:
    print("You can vote.")
else:
    print("You CANNOT vote.")