# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

#Concatinate
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
# print('My name is {name} and  I am {age}'.format( age = age,name = name))

#F_Strings
# print(f'Hello my name is {name} and I am {age}')

# String Methods

s = 'hello world'

#Capitalize string
print(s.capitalize())

#lowerCase
print(s.lower())

#SwapCase
print(s.swapcase())

#Replace
print(s.replace('world','everyone'))

#Count
sub = 'l'
print(s.count(sub))

#Starts with
print(s.startswith('hello'))

#Ends with
print(s.endswith('d'))

#Split into a list
print(s.split())

#find position
print(s.find('r'))

#Is All alphanumeric
print(s.isalnum())

#is alphabetic
print(s.isalpha())

#is all numeric
print(s.isnumeric())