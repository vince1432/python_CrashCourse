# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#Create tuple
fruits = ('Apples','Oranges', 'Grapes')
#fruit = (tuple(('Apple','Grapes')))

#single value needs comma
fruits2 = ('Apple',)

#get value
print(fruits[1])

#Get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

#create sets
fruits_sets = {'Apples', 'Oranges','Grapes'}

#check if in set
print('Apples' in fruits_sets)

#Add to set
fruits_sets.add('Grape')

#Remove from set
fruits_sets.remove('Grape')

#Clear set
fruits_sets.clear()

#delete
del fruits_sets

print(type(fruits_sets))