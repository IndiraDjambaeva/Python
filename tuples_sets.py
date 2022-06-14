# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#simple tuple
fruit_tuple = ("Apple", "Orange", "Mango")
print(fruit_tuple)

#using constructor
fruit_tuple1 = tuple(("Apple", "Orange", "Mango"))
print(fruit_tuple1)

#get single value
print(fruit_tuple1[1])

#can not change value
#fruit_tuple1[1] = "Grape"
print(fruit_tuple1)

#Tuples with one value should have trailing comma
fruit_tuple2 = ("Apple", )
print(fruit_tuple2)
del fruit_tuple2

#get length of tuple
print(len(fruit_tuple1))

# A set is a collection which unordered and unindexed. No duplicate members.

#Create set
fruit_set = {"Apple", "Orange", "Mango", "Apple" }
print(fruit_set)

#Check if in set 
print("Apples" in fruit_set)

# Add to set
fruit_set.add("Grape")
print(fruit_set)

# Add to set
fruit_set.remove("Grape")
print(fruit_set)

#Clear set 
fruit_set.clear()
print(fruit_set)

#Delete set
del fruit_set
print(fruit_set)