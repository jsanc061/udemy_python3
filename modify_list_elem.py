# change, add, and remove elements
letters = ['a','b','c','d','e','f']

letters[0] = 'p'
letters[1] = 3
letters[2] = 2.1

print(letters)

# appending an element at the end to list
letters.append('g')
print(letters)

# creating a list with a series of appends 
empty_list = []
print(empty_list)

empty_list.append('a')
empty_list.append('b')
empty_list.append('c')
empty_list.append('d')
empty_list.append('e')
empty_list.append('f')
empty_list.append('g')
print(empty_list)

# inserting an element into the list
letters = ['a','b','c','d','e','f']

letters.insert(1,'p')
print(letters)

letters.insert(4,'q')
print(letters)

### Use del when you do need the element anymore
### Use pop() when you need to use the element as you remove it

# removing an element from the list using del
letters = ['a','b','c','d','e','f']
del letters[2]
print(letters)

# remove an element from the list using pop()
letters = ['a','b','c','d','e','f']

# removes last element in the list
letters.pop()

# removes the element at desired index
letters.pop(2)
print(letters)

popped_elem = letters.pop()
print(letters)

# returns the popped element from the list
print(popped_elem)

# shows the data type of the popped element
print(type(popped_elem))

# removing item by value
letters = ['a','b','c','d','e','f']
letters.remove('d')
print(letters)

removed_var = 'b'
letters.remove(removed_var)
print(letters)

# list with duplicated items
letters = ['a','b','c','c','d','e','f']
# removes only the first occurence of the value
letters.remove('c')
print(letters)