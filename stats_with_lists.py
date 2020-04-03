# statistics with lists of numbers

# creates an empty list
sq = []
# generates list by squaring values and then appending to list
for num in range(1,11):
    value = num ** 2
    sq.append(value)
print(sq)

# displays the minimum value in the list
print(min(sq))

# displays the maximum value in the list
print(max(sq))

# displays the sum of the values in the list
print(sum(sq))

sq.append(0)
sq.append(100)
sq.append(101)
sq.append(1)

print(sq)
print(min(sq))
print(max(sq))
print(sum(sq))

sq.append(101)
print(sq)
print(min(sq))
print(max(sq))
print(sum(sq))