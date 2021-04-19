#Write a Python program to print the following string in a specific format .
#Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky."

string="""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky."""

print(string)

#2. Write a Python program to get the Python version you are using.
#python --version


#3. Write a Python program to display the current date and time.
#Sample Output :
#Current date and time :
#2021-04-11 14:43:14

import datetime
now = datetime.datetime.now()
print("Current date and time: ")
print(str(now))

#4. Given two integer numbers return their product. If the product is greater than 1000, then return their sum.

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

prod = n1*n2

if prod > 1000:
    print(n1+n2)

else:
    print(prod)

#5. Given a string, display only those characters which are present at an even index number.
string="how are you"
print("characters which are present at an even index number are:",string[::2])

#6.In given tuple,
tt=(55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99)

#a.      What's the index of 2?
index = tt.index(2)
print('The index of 2 is :', index)

#b.     How many times does 777 occur?
count=tt.count(777)
print(f"777 occured {count} times")

#c.     What is the sum of all the numbers in the tuple?
sum_tt = sum((tt))
print("sum of all the numbers in the tuple:",sum_tt)

#d.     What is the minimum value in the tuple?
print("minimum value in the tuple is:",min(tt))