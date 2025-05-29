# students = []
#
# students.append("Lisa")
# students.append("Rose")
# students.append("Jennie")
# students.append("Jisoo")
#
# print("Student Names:")
#
# for name in students:
#     print(name)


L1 = [1,2,3,4,5,6]
L2 = [2,3,5,7,8,9]

common = list(set(L1) & set(L2))


print(common)


numbers = [5, 6, 8, 9, 7, 10]

num = int(input("Enter the number to search:"))

if num in numbers:
    print(f"{num}, is present in list.")

else:
    print(f"{num},is not present in list.")


a = ["A", "B", "C", "D", "E"]

# rev = a[::-1]
a.reverse()
print(a)
