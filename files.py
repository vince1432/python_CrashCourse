# Python has functions for creating, reading, updating, and deleting files.

#Open file
myFile = open('myfile.txt','w')

#Get some info
print('Name: ',myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

#Write file
myFile.write('I love python ')
myFile.write('and Javascript')
myFile.close()

#Append to file
myFile = open('myfile.txt','a')
myFile.write(' I also like PHP')
myFile.close()

#Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)