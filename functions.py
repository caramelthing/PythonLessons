'''function is a follection of code. to be experienced over and over again. 
also can be a mapping - as seen lower down.

define a function. name it.

def function1():
	print("ahhhh")
	print("ahhhhhh 2")
print("this is outside the function")

function1()   #ive called the function i defined for the first time

function1()
function1()

#also a mapping. taking an input, returning an output. mapping. in on the map come out somewhere else.

def function2(some_argument):
	return 2*some_argument

a=function2(4)
print(a)

#we enter an integer data type as some_argument, some_argument gets operated in the function. then put into the variable/reference to an object named 'a', then i print 'a'.
#this is an example of mapping. mapping input x, to output, 2*x.
#3 is the argument.

b=function2(5)
print(b)

c= function2(200)
print(c)

print(type(function1))

#function which takes 2 arguments . aka maps 2 inouts to an output

def function3(x,y):
	return x+y
a=function3(3,6)
print(a)


#bmi calculator

weight = 98
height = 1.95

def bmifunction(weight, height):
	bmi = weight / (height**2)
	print("bmi: ")
	print(bmi)
	if bmi < 25:
		print("go eat nigga")
	else:
		print("yo put it down G")

a = bmifunction(weight, height)

#as this has print in the function, no need to assign to a variable referencing an object then parsing through a print function.
#its literally a part of th defined functio to print the output after the operators have had their way with the variables.

#adding return operators instead of print in within the function



weight = 75
height = 1.9

def bmifunction(weight, height):
	bmi = weight / (height**2)
	print("bmi: ")
	print(bmi)
	if bmi < 25:
		return str(bmi) + " go eat nigga"
	else:
		return str(bmi) + " yo put it down G"

results = bmifunction(weight, height)
print(results)


#task create a funcion which converts miles to km

miles = 20

def convert(miles):
	kilometres = miles * 1.6
	if kilometres < 42:
		return "aint no marathon, you've ran " + str(kilometres) + " klicks though"
	else:
		legendaryStatus = kilometres - 41.6
		return str(legendaryStatus) + " klicks to go for a marathon"

answer = convert(miles)
print(answer)

#above thrown in if and else flow control, with more variable and concatinatin. so it worka out kms from miles, then tells you how many kms to go before its a marathon
#its the easiest thing in the worls but i have firm grasp of the fundamentals. data types, classes functions. keep labbing.
'''

#makign another function!

calories = 4000

def caloryCount(calories):
	allowance = 3000
	if calories < allowance:
		return " keep on chowing down lil nig!"
	else:
		return "less eating more training big man!"

a = caloryCount(calories)
print(a)

