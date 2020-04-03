# dictionaries -  allow you to store limitless amount of info
# a collection of key-value pairs
# key-value pair is a set of values associated with each other
# syntax:
#           dictionary_name={key1:value1, key2:value2}
# example:  
#           user1={'userid':'john1','password':'abc'}

user={'fname':'john','lname':'doe'}
print(user)

# Access values in dictionary
user={'fname':'john','lname':'doe'}
print("Your last name is " + user['lname'].title())

# Add key-value pairs to the dictionary
user['age']=29
print(user)

print('Your age is ' + str(user['age']))

user2={}
user2['fname']='Jenny'
user2['lname']='Yang'
user2['age']='21'
print(user2)

# modify values in a dictionary
user2['fname']='Jacky'
print(user2)

user2['age']=21
print(user2)

if user2['fname']=='Jacky':
    print("Hello " + user2['fname'] + ", how are you?")
else:
    print("Hello user 2" + ", how are you?")
    
user2['fname']='Jenny'
print(user2)

if user2['fname']=='Jacky':
    print("Hello " + user2['fname'] + ", how are you?")
else:
    print("Hello unknown user" + ", how are you?")
    
# removing key-value pairs - permanently
user={'fname':'john','lname':'doe', 'age':29}
print(user)
del user['age']
print(user)