cars = ["mazda", "bmw","audi","ferrari","lambordhini"]
# makes a slice from cars starting at first item and ending at last item
# copies slices of cars into new_list
# NOTE: these two lists are completely separate from each other 
new_list = cars[:]

print(new_list)
print(cars)

cars.append("toyota")
new_list.append("hyundai")

print(cars)
print(new_list)

# creates a new list referenced to the original
new_cars = cars
print(new_cars)
