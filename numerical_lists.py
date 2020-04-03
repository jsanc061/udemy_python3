# using the range() method - excludes last value in range

for value in range(1,5):
    print(value)
    # outputs - 1 2 3 4
    
# using range() to make a list of numbers
numbers = list(range(1,6))
print(numbers)
# output - 1, 2, 3, 4, 5

numbers = list(range(1,15,2))
print(numbers)
# output - 1, 3, 5, 7, 9, 11, 13

numbers = list(range(2,15,2))
print(numbers)
# output - 2, 4, 6, 8, 10, 12, 14

# creates an empty list
sq = []
# generates list by squaring values and then appending to list
for num in range(1,11):
    value = num ** 2
    sq.append(value)
print(sq) 