# organizing a list using the sort() method - permanently sorted
letters = ['b','a','d','e','f','g']
print(letters)
letters.sort()
print(letters)

# prints the list in reverse order - descending sort
letters.sort(reverse = True)
print(letters)

# organizing a list using the sorted() method - temporary sorting
letters = ['b','a','d','e','f','g']
print(letters)
sorted(letters)
print(sorted(letters))
    # outputs sorted list temporarily
print(letters)
    # original list remains the same - unsorted
 
print(sorted(letters, reverse = True))

letters = ['b','A','d','E','g','f','c']
print(letters)
print(sorted(letters))
    # output is not correctly sorted

# print a list in reverse order - permanent change
cars = ['bmw','audi','toyota','hyundai']
print(cars)
cars.reverse()
print(cars)

# find the length of a list using len()
cars = ['bmw','audi','toyota','hyundai']
print(len(cars))

# avoiding index errors with lists
cars = ['bmw','audi','toyota','hyundai']

