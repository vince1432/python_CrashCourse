# A List is a collection which is ordered and changeable. Allows duplicate members.

#Create list
numbers = [1,2,3,4,5]
fruits = ['Apples','Oranges', 'Grapes', 'Pears']

#user Constructor
# numbers2 = list((1,2,3,4,5))

#get Value
print(fruits[1])

#get length
print(len(fruits))

#Append
fruits.append('Mangoes')

#Remove
fruits.remove('Grapes')

#Insert Position
fruits.insert(2,'Strawberry')

#change value
fruits[0] = 'Blueberries'
#remove position
fruits.pop(2)

#Reverse
fruits.reverse()

#Sort
fruits.sort()

#reverse sort
fruits.sort(reverse=true)


print(fruits)
