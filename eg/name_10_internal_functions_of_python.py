# Ten Built-in Functions, you say? Okay, here you go.
#
# complex()- Creates a complex number.
#
print(complex(3.5,4) )
# (3.5+4j)
#
# eval()- Parses a string as an expression.
#
print(eval('print(max(22,22.0)-min(2,3))'))
# 20
#


# filter()- Filters in items for which the condition is true.
#
print(list(filter(lambda x:x%2==0,[1,2,0,False])))
# [2, 0, False]


#
# format()- Lets us format a string.
#
a , b = 2,2
print("a={0} but b={1}".format(a,b))
# a=2 but b=3


# hash()- Returns the hash value of an object.
#
print(hash(3.7))
# 644245917


# hex()- Converts an integer to a hexadecimal.
#
print ( hex(14) )
# ‘0xe’


# input()- Reads and returns a line of string.
#
# print(input('Enter a number'))
# Enter a number7
# ‘7’

# len()- Returns the length of an object.
#
print(len('Ayushi'))
# 6


# locals()- Returns a dictionary of the current local symbol table.
print(locals())
# {‘_name’: ‘main’, ‘doc’: None, ‘package’: None, ‘loader’: <class ‘_frozen_importlib.BuiltinImporter’>, ‘spec’: None, ‘annotations’: {}, ‘builtins_’: <module ‘builtins’ (built-in)>, ‘a’: 2, ‘b’: 3}


# open()- Opens a file.
#
file=open('tabs.txt','w+')
