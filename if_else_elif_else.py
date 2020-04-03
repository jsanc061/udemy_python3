age = 10
if age >= 18:
    print("You can vote.")
else:
    print("Sorry, you cannot vote.")    
    
    
age = 21
if age <= 12:
    price = 5   
elif age >= 13 and age <= 17:
    price = 10
else:
    price = 15
print("Admission charge is $" + str(price))

# multiple elif blocks
age = 66
if age <= 12:
    price = 5
elif age >= 13 and age <= 17:
    price = 10
elif age >= 65:
    price = 7.5
else:
    price = 15
print("Admission charge is $" + str(price))

# test multiple conditions
cars=['audi','bmw','toyota','ferrari','Hyundai']
if 'bmw' in cars:
    print("Nice car!")
if 'audi' in cars:
    print("not too bad")
if 'mazda' in cars:
    print("nice mazda")
    
cars=['audi','bmw','toyota','ferrari','Hyundai']
if 'bmw' in cars:
    print("Nice car!")
elif 'audi' in cars:
    print("not too bad")
elif 'mazda' in cars:
    print("nice mazda")
    
# If statements with lists
# checking for special items

cars=['audi','bmw','toyota','ferrari','Hyundai']
for car in cars:
    print("" + car.title() + " is available.")
    
    
cars=['audi','bmw','toyota','ferrari','Hyundai']
for car in cars:
    if car == 'bmw':
        print("BMW is not available.")
    else:
        print("" + car.title() + " is available.")
        
# check for list is empty or not
cars=[]
if cars:
    for car in cars:
        if car == 'bmw':
            print("BMW is not available.")
        else:
            print("" + car.title() + " is available.")
else:
    print("No cars are available.")
    
cars=['toyota']
if cars:
    for car in cars:
        if car == 'bmw':
            print("BMW is not available.")
        else:
            print("" + car.title() + " is available.")
else:
    print("No cars are available.")
    
# using multiple lists
availaible_cars=['audi','bmw','toyota','ferrari','Hyundai']
wish_cars=['mercedes', 'lamborghini']
for car in wish_cars:
    if car in availaible_cars:
        print(""+ car + " is available.")
    else:
        print(""+ car + " is NOT available.")
        
availaible_cars=['audi','bmw','toyota','ferrari','Hyundai','mercedes']
wish_cars=['mercedes', 'lamborghini']
for car in wish_cars:
    if car in availaible_cars:
        print(""+ car + " is available.")
    else:
        print(""+ car + " is NOT available.")