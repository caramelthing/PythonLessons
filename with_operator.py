#using "with and as" to open a file. 
#"as" which is used instead of '='. Its just syntax. "with" opertor will do open without me #having to specify close() for a cleaner look and less i forget. it uses built in funtions: __enter__ and #__exit__

def Openfile():
	with open("/home/timetoburn/blog/linux","rt") as linux:
		print(linux.read())

if __name__ == '__main__':
	Openfile()

#so which opens it and closes the file.
#will upload but ofcourse nbody else is gonna have a file called linu in a directory called blog haha
#ive thrown this under the name operator too so to show this code is run standalone aka not running code and displaying here from another directory
