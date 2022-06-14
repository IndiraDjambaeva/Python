#A Dictionary is a collection which is unordered, changeble and indexed. No duplicate members.

# simple dictionary
person = {
  "first_name": "John",
  "last_name": "Doe",
  "age": 30
}
print(person)

# Using constructor
person = dict(first_name="John", last_name="Doe", age=30)
print(person)

#Access value
print(person["first_name"])
print(person.get("last_name"))

# Add key/value
person["phone"] = "555-555-5555"
print(person)

#get keys 
print(person.keys())

#get values 
print(person.items())

#make copy
person2 = person.copy()
person2['city'] = "Boston"
print(person2)

# remove item
del(person['age'])
person.pop('phone')
print(person)

# clear
person.clear()
print(person)

#get length
print(len(person2))

#list of dict
people = [
  {'name': "Martha", 'age': 40},
  {'name': "Bob", 'age': 20},
]
print(people)
print(people[1]['name'])
