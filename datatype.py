"""Python Data Types
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, 
and different types can do different things.

Python has the following data types built-in by default, 
in these categories:

Text Type:	str " " '' 
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType


"""

# data  = """123456789"""
# print( type(data))

number =22/7

# print(type(number))
# print(number)

# # 3223.455

# # 324j


# print(type(True)) 


# middle = None
# print(type(None))


# a = []
# a=()
a=range(3)
print(type(a))

"""
Setting the Data Type
In Python, the data type is set when you assign a value to a variable:

Example	                                             Data Type	
x = "Hello World"	                                   str	
x = 20	                                               int	
x = 20.5	                                           float	
x = 1j	                                               complex	
x = ["apple", "banana", "cherry"]	                    list	
x = ("apple", "banana", "cherry")	                    tuple	
x = range(6)	                                        range	
x = {"name" : "John", "age" : 36}	                    dict	
x = {"apple", "banana", "cherry"}	                     set	
x = frozenset({"apple", "banana", "cherry"})	       frozenset	
x = True	                                             bool	
x = None	                                          NoneType"""


fn = " kofi"
ln ="kumi "

# print(fn[start:end])

# print(ln.upper())

fn = fn + ' '+ ln
# print(fn)


# newdata = fn.strip()
# print(newdata.capitalize())
# b=fn.replace("k","q")
# print(b)
# x= 1
# a = x

# print(a)



# a = "Hello World!"
# first = a.split('l')
# # print(first[0])
# # print(first[1])
# print(first)


fn ="komi John kofi"
# sn = fn[:3]
# print("hello Mr " + sn)

sn = fn.split(' ') 
print(sn)

# print("hello Mr " + sn)

name = "nana ama"
newName = name.split(' ')
again = newName[0] 
print(again.upper())

"""Exercise:
Use the len method to print the length of the string.
x = "Hello World" """

# x = "Hello World" 
# print(len(x))


# Get the first character of the string txt.
txt = "Hello World"
print(txt[0])



# Get the characters from index 2 to index 4 (llo).
# txt = "Hello World"


# return the string without any whitespace at the beginning or the end.
# txt = " Hello World "



# Convert the value of txt to upper case.
# txt = "Hello World"


# Convert the value of txt to lower case.
# txt = "Hello World"

# replace the character H with a J.
# txt = "Hello World"