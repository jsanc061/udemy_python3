# tuple - an immutable list (cannot change values) 
rect_dim=(100,50)
print(rect_dim)

print(rect_dim[0])
print(rect_dim[1])

rect_dim[0] = 150
    # output - TypeError: 'tuple' object does not support item assignment