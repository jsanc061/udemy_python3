# list of dictionaries

# creates two dictionaries
user1={'name':'abc','age':28}
user2={'name:':'def','age':25}

# nests two dictionaries into a list
users=[user1,user2]
for u in users:
    print(u)
    
# creates an empty list
enemies=[]
# appends dictionary to the list to create 20 enemies
for enemy_num in range(20):
    enemy_dict={'color':'black','points':10}
    enemies.append(enemy_dict)
print(enemies)
print("Total enemies created: " + str(len(enemies)))

for e in enemies[:3]:
    print(e)    # returns the first 3 elements in the list
    
for e in enemies[:5]:
    if e['color']=='black':
        e['color']='green'
print(enemies)  # replaces color attribute for the first 5 elements in the list

# nested list in dictionaries
user={'name':'John','hobbies':['singing','dancing','painting'],}
print(user)
print(user['hobbies'])

print("List of hobbies for user: " + user['name'])
for hobby in user['hobbies']:
    print("\n"+ hobby)
    
users={'user1':['reading','singing'], 'user2':['dancing','surfing']}
print(users['user1'])
print(users['user2'])

# nested dictionary in another dictionary
users={'user1':{'name':'John','hobby':'reading',},'user2':{'name':'Bob','hobby':'gaming'}}
for user_name,user_hobby in users.items():
    print("Logged in as: " + user_name)
    print(user_hobby)
    
# iterates over the dictionary key-value pairs
for user_name,user_hobby in users.items():
    print(user_hobby)
    

for user_name,user_hobby in users.items():
    print("Logged in as: " + user_name)
    print("\tName: " + user_hobby['name'])
    print("\tHobbies: " + user_hobby['hobby'])
    
person1={'first_name':'John'}
person2={'last_name':'Doe'}
person=[person1,person2]

for p in person:
    print(p)
    
Cities={'Austin':{'country':'US'},'Dallas':{'country':'US'},'San Antonio':{'country':'US'}}
print(Cities)