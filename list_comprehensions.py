# list comprehension - combines the for loop and creation of new elements in one line

# traditional way of creating a list
sq = []
# generates list by squaring values and then appending to list
for num in range(1,11):
    value = num ** 2
    sq.append(value)
print(sq)

# generates same as list above but combined into one line of code
sq = [value for value in range(1,11)]
print(sq)