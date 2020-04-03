# simple example
cars = ["mazda", "bmw","audi","ferrari","lamborghini"]
for car in cars:
    if car == 'audi' or car == 'bmw':
        print(car.upper())
    else: 
        print(car.title())
        
# checking for equality
cars = ["mazda", "bmw","Audi","ferrari","lamborghini"]
for car in cars:
    if car == 'audi' or car == 'bmw':
        print(car.upper())
    else: 
        print(car.title())

name = 'Josh'
if name == 'josh':
    print("Matched")

# comparing capitalized and lower-cased string values    
name = 'Josh'
if name.lower() == 'josh':
    print("Matched")
    
# checking for inequality (!=)
name = 'Jack'
if name !='Jill':
    print("No match")
    
name = 'Jack'
if name =='Jill':
    print("No match")
    
# numerical comparisons
age = 29
if age == 29:
    print("match")

age = 29
if age != 28:
    print("Do not match")

age = 29
age < 20    # false
age <= 20   # false   
age > 20    # true
age >= 20   # true

# multiple conditions using 'and'
age = 29
your_age = 20
print(age >= 21 and your_age >= 21)    # false

age = 29
your_age = 21
print(age >= 21 and your_age >= 21)    # true

# multiple conditions using 'or'
age = 29
your_age = 21
print(age >= 21 or your_age >= 21)     # true

age = 29
your_age = 20
print(age >= 21 or your_age >= 21)     # true

age = 19
your_age = 20
print(age >= 21 or your_age >= 21)     # false


# check if the value is in a list using 'in' keyword
cars = ["mazda", "bmw","audi","ferrari","lamborghini"]
print('bmw' in cars)    # true
print('toyota' in cars) # false

# check if the value is NOT in a list using 'not in' keyword
cars = ["mazda", "bmw","audi","ferrari","lamborghini"]
print('bmw' not in cars)    # false

your_car = 'toyota'
if your_car not in cars:
    print("Your car " + your_car.title() + " is not on the list")
    
