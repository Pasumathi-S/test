
"""write a python code to print the output"""
# comment start
import random

print("welcome to python!")
print("I am leaning variables and data types")

"""creating variables for int,float,str,complex and finding that type and also printed that vales"""
x,y,z,a=1,2.5,"joy",1+2j
b=x,y,z,a
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(b)

""" creating list with adding and remove vales using append and remove/pop"""
# If we use pop we need to mention the specified index or key.
# If we use remove we can mention the value which is declared.

color=["b","o","y"]
color.append("g")
color.pop(2)
print(color)
color.extend([1,2,3])
color.extend(color)
print(color)

""" creating tuple and print the values"""
color= ("b","o","y")
print(color)

# Creating a dictionary
my_dict={"name": "Joy", "Age": 25,"City":"Chennai"}
print(my_dict)

# Accessing values
print(my_dict["name"])
print(my_dict["Age"])

# Adding or modifying elements
my_dict["Occupation"]="Developer"
my_dict["Exp"]= 5
print(my_dict)

# Deleting elements and printing values
del my_dict["City"]
print(my_dict)

# Iterating through keys and values
for key, value in my_dict.items():
    print(key, value)

# created the set I added and removed the vales on set
my_set={"apple","Orange","cherry", "apple"}
my_set.add("mango")
print(my_set)
my_set.remove("cherry")
print(my_set)

# boolean type
x=1
if x >= 1:
    print("true")
else:
    print("False")


# Boolean bytes
x=bytes([65,66,67])
print(x)
print(x[0])

# Bytearray
x=bytearray([65,66,67])
x[0]=70
print(x)

# encoding and decoding, Memeoryview,Slice
b=bytearray("hello", "utf-8")
c=memoryview(b)
print(c[1])
c[0]=80
slice_c=c[0:1]
print(slice_c.tobytes())
#print(c)

# None type
def greet():
    print("hello!")

result=greet()
print(result)

# global variables and also local variable
x="awsome"
def myfunc():
     x="lovely"
     print("python is " + x)
myfunc()
print("python is " + x)

# python Numbers + Random
x=1
y=50
a=0.0
b=0.9
print(random.randint(x,y))
print(random.uniform(a,b))

f=36e8
print(f)


print(r"C:\new_folder")






















