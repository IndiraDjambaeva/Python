name = "Brad"
age = 37

#Concatenate
print("Helo World")
#print("Helo I am " + name + " and I am " + age) # error TypeError: can only concatenate str (not "int") to str

print("Helo I am " + name + " and I am " + str(age))

#String Formatting

#Argumnets by position
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

#Argumnets by name
print("My name is {name} and i am {age}".format(name="Tim", age="39"))
print("My name is {name} and i am {age}".format(name=name, age=age))

#F-Strings (only in 3.6+)
print(f'My name is {name} and I am {age}')

#String Methods
s = "hello there world"

#Capitalize first letter
print(s.capitalize())

#Make all uppercase
print(s.upper())

#Make all lower
print(s.lower())

#Swap case
print(s.swapcase())

#Get length 
print(len(s))

#Replace
print(s.replace('world', "everyone"))

#Count
sub="h"
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

#Split into a list
print(s.split())

#Find position 
print(s.find("r"))

#Is all alphanumeric
print(s.isalnum())

#Is all alphabetic
print(s.isalpha())

#Is all numeric
print(s.isnumeric())



