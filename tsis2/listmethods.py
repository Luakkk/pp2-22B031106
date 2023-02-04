a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

a.append(b)

print(a)
#Adds an element at the end of the list




fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits)
#Removes all the elements from the list




fruits = ["apple", "banana", "cherry"]

x = fruits.copy()

print(x)
#Returns a copy of the list




fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)
#Returns the number of elements with the specified value




fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)
#Add the elements of a list (or any iterable), to the end of the current list





fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)
#Returns the index of the first element with the specified value




fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)
#Adds an element at the specified position





fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)
#Removes the element at the specified position





fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")

print(fruits)
#Removes the item with the specified value



fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)
#Reverses the order of the list




cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)
#Sorts the list
