'''List type method, sort

spam = [-2, 3.14, -7, 2, 9, 7]
spam.sort()
print(spam)

zoo = ["zebra", "white lion","ant", "policeman"]
zoo.sort()
print(zoo)

zoo.sort(reverse=True)
print(zoo)

#sorts the list in place, no good spam - spam.sort()
#with a number and string value

bag = ["books", "shiney new laptop", "the internet", 5, 3.69, "dam she's fine"]
bag.sort()
print(bag)

#3.ASCIIbetical, capitaised Zoo, comes before lower case ant
'''
zoo = ["zebra", "white lion","ant", "policeman", "Zoo", "Xylophone playing Trump"]
zoo.sort(key=str.lower)
print(zoo)