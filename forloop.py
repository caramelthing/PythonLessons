#for loop

mylist = ["a", "b", "c", "d"]
print(mylist)

for character in mylist:
	print(character)


#nice way to iterate through a list

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
	print('Index ' + str(i) + ' in supplies is: ' + supplies[i])