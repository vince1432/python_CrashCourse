# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#Create dictionary
person = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age' : 30
}

#get value
print(person['first_name'])
print(person.get('last_name'))

#add key/value
person['phone'] = '55-555-5555'

#get dict keys
print(person.keys())

#get items
print(person.items())

#Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove Item
del(person['age'])
person.pop('phone')

#clear
# person.clear()

#Get length
print(len(person))

#list of dict
people = [
    {'name' : 'Martha', 'age' : 30},
    {'name' : 'Kevin', 'age' : 25}
]

print(people[0]['name'])