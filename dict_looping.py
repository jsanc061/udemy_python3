# looping through key-value pairs
user_age={
    'John':31,
    'Tom':26,
    'Tim':28,
    'Jack':30
}
print(user_age)

# items() returns a list of key-value pairs
for key,value in user_age.items():
    print("Name: " + 
          key + 
          "\tAge: " + 
          str(value) + 
          "\n")
    

user={'fname':'john','lname':'doe', 'age':29}
for a,b in user.items():
    print("Key: "+a)
    print("Value: "+str(b))
    
# looping through keys only
user_age={
    'John':31,
    'Tom':26,
    'Tim':28,
    'Jack':30
}
print(user_age)

# keys() returns a list of all the keys
for name in user_age.keys():
    print("Hello "+ name + "!")
    
# looping through values only
# values() returns a list of all the values
for age in user_age.values():
    print("The list of ages are shown as followed: " + str(age))
    
if 'John' in user_age.keys():
    print("John, Welcome!")
    
# print a message to a specific user
for a in user_age:
    if a=='John':
        print("John, Welcome!")

# sorting keys while looping through a dictionary
user_age={
    'John':31,
    'Josh':25,
    'Tom':26,
    'Tim':28,
    'David':35,
    'Jack':30
}

print("\nUnsorted names:\n")

for a in user_age.keys():
    print("Hello " + a)

print("\nSorted names:\n")

for a in sorted(user_age.keys()):
    print("Hello " + a)

# sorted() affects list temporarily
print(user_age)

# looping through values
user_age={
    'John':31,
    'Josh':25,
    'Tom':26,
    'Tim':28,
    'David':35,
    'Jack':30
}

# prints all ages in the dict
print("List of ages of all users:")
for a in user_age.values():
    print(str(a))
    
# checking for duplicate key-value pairs
user_age={
    'John':31,
    'Josh':25,
    'Tom':26,
    'Tom':26,
    'Tim':28,
    'Fred':35,
    'David':35,
    'Jack':30
}
print(user_age) # only prints one instance where duplicate keys occur; does not affect duplicate values

# set() builds an unordered list of non-duplicated items
# set() cannot have mutable items
print("\nList of values excluding duplicates:\n")
for a in set(user_age.values()):
    print(a)

# prints all values including duplicates
print("\nAll values including duplicates:\n")
for a in user_age.values():
    print(a)

# Tom and David's age are set to the second instance values; 27 and 35   
user_age={
    'John':31,
    'Josh':25,
    'Tom':26,
    'Tom':27,
    'Tim':28,
    'Fred':35,
    'David':33,
    'David':35,
    'Jack':30
}
print(user_age)

# Q1
user={'First_Name':'John','Last_Name':'Doe','Age':25}

print(user['First_Name'])
print(user['Last_Name'])
print(user['Age'])

# Q2
user['First_Name']='James'
print(user['First_Name'])

# Q3
for a in user.keys():
    print(a)

# Q4    
for a in user.values():
    print(a)