#using "with" to read a file and "as" which is used to instead of =. just syntax, "with" opertor will do that without me haing to specify close() for a cleaner look and less i forget. it used _enter_ and _exit_


def Openfile():
	with open("/home/timetoburn/blog/linux","rt") as linux:
		print(linux.read())

if __name__ == '__main__':
	Openfile()

#so which opens it, pritns it and closes
#will upload this anyway but wont run as its gotta call this file
#ive thrown this under the name operator too so to show this code is run standalone aka not running code and displaying here from another directory