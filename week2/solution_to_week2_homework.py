# 1.Write a function called fizz_buzz that takes a number
# a. If the number is divisible by 3, it should return “Fizz”.
# b. If it is divisible by 5, it should return “Buzz”.
# c. If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# d. Otherwise, it should return the same number.

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("fizz buzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)

number=int(input("enter a number:"))
fizzbuzz(number)

#2.Consider a lst= [5, 10, 20] and write a try and except block to avoid IndexError.

lst= [5, 10, 20]

def find_index(n):
    try:
        print(lst[n])
    except IndexError:
        print("index not found")


find_index(4)

#3.Create a class of Jet inventory with two arguments i.e name and country.
# Also add the minimum 2 items in the class and print them.

class Jet:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def jet_Info(self):
        print(f'{self.name} is a {self.country} airline')


myjet = Jet("SAS", "Scandinavian")
myjet.jet_Info()

#5.Write a Python script to check whether a given key already exists in a dictionary.
# Dictionary Initialisation
My_Dict = {'1':'Joy', '2':'John', '3':'Joye', '4':'Jiya'}

for key, value in My_Dict.items():
    print(key, value)


def guess_key(input_key):
    if input_key in My_Dict:
        print(f'key entered -  {input_key}  is found')
    else:
        print(" No  key found!")


user_key = input("which key do you want to guess?\n")
print('user_key ', user_key)
guess_key(user_key)

#6.Write a function called showNumbers that takes a parameter called limit.
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
#For example, if the limit is 3, it should print:
#0 EVEN
#1 ODD
#2 EVEN
#3 ODD

def shownumber(limit):
    for i in range(limit+1):
            if i % 2 == 0:
                print(f"{i} EVEN")
            else:
                print(f"{i} ODD")


limit_number=int(input("enter a limit number:"))
shownumber(limit_number)

#8.Create a class named Person, with firstname and lastname properties, and a print name method.

class Person:
    def __init__(self, firstname,lastname):
        self.first_name = firstname
        self.last_name = lastname

    def print_name(self):
        print(f' Person Name is : {self.first_name} {self.last_name}')


person_name = Person("Mamatha","Mereddy")
person_name.print_name()

#9.Write a program asks for numeric user input. Instead the user types characters in the input box.
# The program normally would crash. But write try-except block so it can be handled properly.

def numeric_user_input():
    try:
        user_input=int(input("enter a number:"))
        print(user_input)
    except ValueError:
        print("invalid input,try to enter a number")

numeric_user_input()

#10.Write a Python program to create two empty classes, Student and Marks.
# Now create some instances and check whether they are instances of the said classes or not.
# Also, check whether the said classes are subclasses of the built-in object class or not.

class Student:
    pass

class Marks:
    pass

student1 = Student()
marks1 = Marks()

print(isinstance(student1, Student))
print(isinstance(marks1, Marks))

print("\nCheck whether the said classes are subclasses of the built-in object class or not.")

#print(issubclass(Student, Marks))
print(issubclass(Student, object))
print(issubclass(Marks, object))