""" age = 28
message = "happy " + age + "th birthday!"
print(message) """

# produces the error
# TypeError: can only concatenate str (not "int") to str

# Solution to this type error

age = 28
message = "happy " + str(age) + "th birthday!"
print(message)


# the str() method converts int to string