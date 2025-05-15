# # age=18
# # if age>=18:
# #     print("you are eligible to vote")
# #
# #
# # name="Alice"
# # print(type(name))
# #
# #
# # a,b,c=1,2,3
# # x=a,b,c
# # print(x)
# # print(a)
# # print(b)
# # print(c)
# #
# #
# # y=10
# #
# # def myfunc():
# #   global y
# #   y=y+5
# #   print("Inside Myfunc:",y)
# #
# # myfunc()
# # print("Outside myfunc:",y)
#
#
# s="Hello World"
# x=1
# l=[1,2,3,4]
# d={"name":"Alice","age":15}
# set={1,2,3,4}
# # b=true
# b=b'hello'
# # x=none
#
# print(type(s))
# print(type(x))
# print(type(l))
# print(type(d))
# print(type(set))


# text="Hello python"
#
# encoded_text=text.encode('utf-8')
# print("encoded:",encoded_text)
#
# decoded_text=encoded_text.decode('utf-8')
# print("decoded:", decoded_text)


# x=1
# y=2.1
# z=2+1j
#
# print(x,y,z)


# import random
#
# random_number=random.randint(1,100)
# print("Ramdom Number:",random_number)


# num=3.14523
# round_num=round(num,2)
# print(round_num)


# a=5.6
# a_int=int(a)
# print(a_int)
#
# b=1
# b_float=float(b)
# print(b_float)

# for char in "python":
#     print(char)

# x="Hello World!"
# print(len(x))

# text="data science"
#
# if "data" in text:
#     print("yes data is present")
# else:
#     print("no data is not present")

# text="python"
# print(text[-4:])

# text= "I learn Python"
# print(text[2:7])
#
# x="hello"
# # y=x.upper()
# print(x.upper())

# text="I love Python"
# update_text= text.replace("Python","Java")
# print(update_text)

# test=" I love India "
# update_space=test.replace(" ","")
# print(update_space)

# l_name="alice"
# s_name="Joe"
# f_name= l_name+ " " + s_name
# print(f_name)

# name="John"
# age=25
#
# sentence = "My name is {} and I am {}.".format(name,age)
# print(sentence)

# price=4.663222
# format_price="price: {:.2f}".format(price)
# print(format_price)

# print("she said ,\"hello\" ")
text = "   Hello Python World  "
# print(text.upper())
# print(text.lower())
# print(text.replace("Python","Java"))
# print(text.strip())
# print(text.split())

# x=int(input("Enter the number:"))
# if x > 100:
#     print("True")
# else:
#     print("False")

# x="I like python"
# if "python" in x:
#     print("True")
# else:
#     print("False")

# def myfunc(text):
#     return "python" in text
#
# print(myfunc("I am learning python"))
# print(myfunc("I am learning java"))

# num1 = float(input("Enter first number:"))
# operator = input("Enter operator(+,-,*,/): ")
# num2=float(input("Enter the second number:"))
#
# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif  operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     if num2 !=0:
#       result = num1 / num2
#     else:
#         result = "cannot divide by zero"
# else:
#     result = "Invalid operator"
#
# print(result)

# a = int(input("Enter first number :"))
# b = int(input("Enter the second number:"))
#
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

# a=[1,2,3,4]
# b=a
# c=[1,2,3,4]
#
# print(a is b)
# print(a is c)
# print(c is not a)
# print( 4 in a)
# print( 5 not in c)
#
# text = "learning python"
# print("python" in text)
# print("java" not in text)

# fruits = ["apple", "banana", "orange"]
# print(fruits[1])
# fruits.append("mango")
# print(fruits)

# my_list1 = [40,50,60,10,20]
# my_list2 = [30,70,80]

#my_list= my_list1.copy()
# join_my_list= my_list + my_list2
# print(join_my_list)

# my_list1.extend(my_list2)
# print(my_list1)
# my_list.sort()
# my_list.sort(reverse=True)
# print(my_list)

# square = [x**2 for x in range(1,11)]
# print(square)
#
# my_tuple=("apple","banana","cherry","date")
# # print(my_tuple[0])
# a,b,c,d = my_tuple
# print(a)
# print(b)
# print(c)

# tuple1 = ("apple","mango")
# tuple2 = ("orange","cherry")
# tuple_new = tuple1+tuple2
# print(tuple_new)
# for item in tuple_new:
#     print(item)

# set1={1,2,3,4,5}
# print(set1)
#
# set1.add(6)
# print(set1)
#
# set1.remove(4)
# print(set1)
#
# set2= {4,5,6,7,8}
#
# print(set2)
#
# union_set= set1.union(set2)
# print(union_set)
#
# Intersection_set= set1.intersection(set2)
# print(Intersection_set)

# student1= {"name": "hari","age": 20,"marks": 80}
# print(student1["name"])
# print(student1["age"])
#
# student1["grade"] = "A"
# print(student1)
#
# student1.pop("marks")
# print(student1)

# student = {
#     "student1":{"name":"hari","age": 20,"marks": 70},
#     "student2":{"name":"priya","age": 19,"marks":80}
#            }
# print(student["student1"]["name"])
#
#
# print("Looping through student data:")
# for key, value in student.items():
#     print(key, ":", value)

# age =18
# if age>=18:
#     print("this person is eligible to vote")
# else:
#     print("this person is not eligible to vote")

# day = 4
#
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid input. Enter a number between 1 and 7.")

# num=1
#
# while num<=20:
#     print(num)
#     num += 1

# fruits=["apple","banana","cherry"]

# for fruit in fruits:
#     if fruit == "apple":
#         continue
#     print(fruit)
# rows = 5
#
# for i in range(1, rows+1):
#     for j in range(i):
#         print("*",end="")
#     print()


# for i in range(1, 6):
#     print(i)
# else:
#     print("For loop finished without break.")
# x = 1
# while x <= 5:
#     print(x)
#     x += 1
# else:
#     print("While loop finished without break.")


# def factorial(n):
#     if n < 0:
#         return
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# # Example usage
# num = 5
# print(f"Factorial of {num} is {factorial(num)}")

# def sum_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     print("Sum:", total)
#
# # Example usage
# sum_numbers(10, 20, 30)
# sum_numbers(5, 15)

# def print_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# # Example usage
# print_details(name="Alice", age=25, course="Python")

# square = lambda x: x**2
# print(square(8))

# students = [("alice",88),("bob",65),("john",70)]
# students.sort(key=lambda x: x[1])
# print(students)

# import array
#
# nums=array.array('i',[1,2,3,4,5,6])
#
# nums.append(7)
# nums.insert(2,8)
#
# print(nums)
#
# nums.remove(5)
# nums.pop()
#
# print(nums)
#
# print("square of element:")
# for num in nums:
#     print(num*2)
#
# class car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#
#     def display_details(self):
#         print(f"car Brand:{ self.brand}")
#         print(f"car model:{self.model}")

# car1=car("toyota","innova")
# car1.display_details()
#
# car1.model="fortuner"
# print("\nafter modifying the model:")
# car1.display_details()
#
# del car1.brand
# print("\nafter delete the brand:")
# print(vars(car1))

# class electriccar(car):
#     def __init__(self,brand,model,battery_capacity):
#        super().__init__(brand,model)
#        self.battery_capacity=battery_capacity
#
#     def display_details(self):
#         super().display_details()
#         print(f"battery capacity: {self.battery_capacity} kwh")
# e_car=electriccar("tesla","model3",75)
# e_car.display_details()

# class MyNumbers:
#     def __iter__(self):
#         self.num = 1
#         return self
#     def __next__(self):
#         if self.num < 5:
#             val = self.num
#             self.num += 1
#             return val
#         else:
#             raise StopIteration
#
# my_iter=MyNumbers()
# iterator=iter(my_iter)
#
# for number in iterator:
#     print(number)

# def add(a,b):
#     if type(a) == type(b):
#         return a + b
#     else:
#         return "Error: Both inputs must be of the same type(int, float, or str)"
#
# print(add(10 , 5))
# print(add("Hi","Hello"))
# print(add(3.5, 2.5))
# print(add("hello", 5))

# class Animal:
#     def speak(self):
#         print("The animal makes a sound")
#
# class Dog(Animal):
#     def speak(self):  # Overriding the speak method
#         print("The dog barks")
#
# class Cat(Animal):
#     def speak(self):  # Overriding the speak method
#         print("The cat meows")
#
# for animal in (Dog(), Cat(), Animal()):
#     animal.speak()

# def my_func():
#     x=1
#     print(x)
#
# my_func()

# age = int(input("Enter your age: "))
# print(age + 5)  # ✅ Works fine


product = input("Enter product name: ")
price = float(input("Enter product price: "))

print(f"{product} costs ₹{price:.2f}")


























