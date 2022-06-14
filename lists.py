# Create list
numbers = [1,2,3,4,5]
print(type(numbers))
print(numbers)

# Using a constructor
numbers1 = list((1,2,3,4,5))
print(numbers1)

# Using a constructor
numbers1 = list((1,2,3,4,5))
fruits = ["Apples", "Oranges", "Grapes",  "Pears", 12]
print(numbers1)
print(fruits)

#get value
print(fruits[1])

#get length
print(len(fruits))

#append to list
fruits.append("Mangos")
print(fruits)

#remove from list
fruits.remove("Grapes")
print(fruits)

#insert into position
fruits.insert(2, "Strawberries")
print(fruits)

#remove from position
fruits.pop(3)
print(fruits)

# reverse list
fruits.reverse()
print(fruits)

#sort list
fruits1 = ["Apples", "Oranges", "Grapes",  "Pears"]
fruits1.sort()
print(fruits1)

#reverse sort
fruits1.sort(reverse=True)
print(fruits1)