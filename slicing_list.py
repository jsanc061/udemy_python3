# slicing elements in a list
letters = ['a','b','c','d','e','f']
print(letters[0:4])

print(letters[:4])

print(letters[3:])

print(letters[3:6])

# prints all elements in list by step size of 1
print(letters[::])
# output: a, b, c, d, e, f

# prints all elements in list by step size of 2
print(letters[::2])
# output: a, c, e

# prints all elements in list by step size of 3
print(letters[::3])
# output: a, d

# reverse the elements in the list
print(letters[::-1])

name = 'Josh'
print(name[2])
# output: s

print(name[2:])
# output: sh

print(name[::-1])
# output: hsoJ

# looping through slices
cars = ["mazda", "bmw","audi","ferrari","lamborghini"]
print("First three cars: ")
for first_three in cars[:3]:
    print("\t"+first_three.title())


cars=['bmw','audi','toyota','hyundai','ferrari']

for selected in cars[1:3]:
    print(selected)