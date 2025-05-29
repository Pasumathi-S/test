# # 1.Reverse a String
#
# text = "Hello"
# # reverse_string = text[::-1]
# print(text[::-1])
#
#
# # 2.Check for Palindrome
#
# string = "malayalam"
#
# # if string == string[::-1]:
# #     print("String is palindrome")
#
#
# length = len(string)
# i = 0
# j = length - 1
#
# while i < j:
#     if string[i] != string[j]:
#         print("No,it is not a palindrome")
#         break
#     i += 1
#     j -= 1
# else:
#     print("Yes,it is a palindrome")
#
#
#
# # 3.Find the Factorial (Recursive)
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# number = 5
# result = factorial(number)
# print(f"the factorial of {number} is {result}")
#
# # 4.Find the Second Largest Number in a List
# def second_largest(numbers):
#    unique_numbers = list(set(numbers))
#    unique_numbers.sort()
#    if len(unique_numbers) < 2:
#        return None
#    return unique_numbers [-2]
#
# print(second_largest([10, 20, 4, 45, 99]))
#
# # 5.Write a function that removes duplicates from a list while preserving order.
#
# a = [10, 20, 4, 45, 99, 99, 10, 4, 4]
# b = list(dict.fromkeys(a))
# print(b)
#
# print(list(set(a)))
#
# # 6.Reverse Words in a String
# str = "Python is fun"
# reverse_words = " ".join(str.split()[::-1])
# print(reverse_words)
#
# # 7.Find Missing Numbers in a List
A = [1, 2, 4, 5, 7,9,12]
def missing(A):
    for i in range(len(A)-1):
        current = A[i]
        next_value = A[i+1]

        for num in range(current + 1, next_value):
            print(num)
missing(A)

# def find_missing_number(nums):
#     n = len(nums) + 1
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum
# numbers = [1, 2, 3, 5,7]
# print("Missing number is:", find_missing_number(numbers))

# 8.Count Frequency of Elements
# list1 = [1,1,1,2,2,3,3,4,4,4,5,5,5,6,6,7]
#
# frequency = {}
# for item in list1:
#     if item in frequency:
#         frequency[item] += 1
#     else:
#         frequency[item] = 1
# print(frequency)
#
#
# list2 = ["apple", "apple","lemon","lemon","mango","lemon"]
# frequency = {}
# for item in list2:
#     if item in frequency:
#         frequency[item] += 1
#     else:
#         frequency[item] = 1
# print(frequency)
#
# from collections import Counter
#
# list3 = "I like to learn python"
# frequency = Counter(list3.replace(" ", ""))
# print(dict(frequency))

# 9.Prime Numbers in a Range
# start = 5
# end = 50
#
# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)


# 10.First Non-Repeating Character
# def non_repeat(string):
#     freq = {}
#     for x in string:
#         freq[x] = freq.get(x, 0) + 1
#
#     for i in string:
#         if freq[i] == 1:
#             return i
#     return -1
#
#
# print(non_repeat("aabbccdeeddfgghhii"))

# 11.Find duplicate words from the given sentence and it's repeat count.

# from collections import Counter
# a = "He raced to the grocery store. He went inside but realized he forgot his wallet. He raced back home to grab it." \
#     " Once he found it, he raced to the car again and drove back to the grocery store."
# word = a.split()
#
# count = Counter(word)
#
# for word, freq in count.items():
#     if freq > 1:
#         print(f"{word} : {freq}")


# a = "He raced to the grocery store. He went inside but realized he forgot his wallet. He raced back home to grab it." \
#     " Once he found it, he raced to the car again and drove back to the grocery store."
#
# a = a.lower().replace('.', '')
#
# words = a.split()
#
# word_count = {}
#
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
# for word, count in word_count.items():
#     if count > 1:
#         print(f"{word} : {count}")

# 12.Count the Number of Words in a String

# import re
# string = "I like to learn python 3.5 version!"
#
# print("words:", len(re.findall(r'\b[a-zA-Z]+\b',string)))
# print("character:",len(string.replace(" ","",)))
# print("numbers:", len(re.findall(r'\d+(?:\.\d+)', string)))
# print("special_chars:",len(re.findall(r'[^a-zA-Z0-9\s]', string)))


# 13. Count Vowels in a String

# def count_vowels(string):
#     vowels = "aeiouAEIOU"
#     vowel_present = set()
#     count = 0
#
#     for char in string:
#         if char in vowels:
#             count += 1
#             vowel_present.add(char.lower())
#     print("total vowels present in str:", count)
#     print("vowels present in str:", ", ".join(vowel_present))
#
#
# count_vowels("I am a good girl")


# 14. Check for Anagram
#
# a = "silent"
# b = "listen"
#
#
# def anagram(a, b):
#     return sorted(a) == sorted(b)
#
#
# print(anagram("silent", "listen"))
#
#
# # 15.Write a function to find all unique pairs of numbers in a list that sum up to a given target.
# def find_pairs(lst, k):
#     res = []
#     while lst:
#         num = lst.pop()
#         diff = k - num
#         if diff in lst:
#             res.append((diff, num))
#     res.reverse()
#     return res
#
#
# lst = [1, 5, 3, 7, 9]
# k = 12
# print(find_pairs(lst, k))
#
# # 16.Write a Python function to find the longest word in a given sentence.
#
# s = "I am going to bangalore for study"
# words = s.split()
# result = ""
#
# for word in words:
#     if len(word) > len(result):
#         result = word
# print(result)

# 17. 1. Create a class to represent a Bank Account
# Include methods to deposit, withdraw, and check balance.
#
# Prevent withdrawal if funds are insufficient.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"deposited {amount},New Balance:{self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient amount"
        self.balance -= amount
        return f"withdraw {amount},Remaining Balance: {self.balance}"

    def check_balance(self):
        return f"Balance: {self.balance}"


account = BankAccount("Lisa", 1000)
print(account.deposit(500))
print(account.withdraw(300))
print(account.check_balance())


# 18. 2. Design a class Student with subjects and marks
# Add a method to calculate average and grade.
#
# Use encapsulation to protect data.

class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def calculate_average(self):
        return sum(self.__marks.values()) / len(self.__marks)

    def get_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "D"


student = Student("Lisa", {"maths": 90, "Science": 80, "Maths": 95})
print("Average:", student.calculate_average())
print("grade:", student.get_grade())


# 19. Create a class hierarchy for shapes
# Use inheritance: Base class Shape, and child classes like Rectangle, Circle, etc.
#
# Each should have a method to calculate area.

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


rect = Rectangle(10, 2)
cir = circle(7)
print("Rectangular area:", rect.area())
print("Circular area:", cir.area())


# 20. Build a class for a simple Shopping Cart system
# Add items with price and quantity.
#
# Calculate total cost using a method.

class ShoppingCart:
    def __init__(self):
        self.item = []

    def add_item(self, item, price, quantity):
        self.item.append((item, price, quantity))

    def total_cost(self):
        return sum(price * quantity for item, price, quantity in self.item)


cart = ShoppingCart()
cart.add_item("apple", 140, 3)
cart.add_item("milk", 30, 5)
print("Total cost:", cart.total_cost())


# 21. Demonstrate Polymorphism using a speak() method
# Create a base class Animal with a speak() method.
#
# Subclasses Dog and Cat should override speak().


class Animal:
    def speak(self):
        print("some sound")
        return "some sound"

class dog(Animal):
    def speak(self):

        return "woof!"

class cat(Animal):
    def speak(self):
        super().speak()
        return "meow!"

animals = [dog(),cat()]
for animal in animals:
    print(animal.speak())


