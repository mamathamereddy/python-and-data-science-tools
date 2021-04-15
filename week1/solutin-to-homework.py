# 1. Write a python script to print your name and age
Name = input("Enter  Name:")
age = input("Enter age:")
print(f'Hello {Name.capitalize()} \n You are {age} years old')

# 2. Create a list of your 5 favorite movies and store it in the variable
favourite_movies = []
for i in range(5):

    movie = input(f'enter your {i + 1} favourite movie:')
    favourite_movies.append(movie)

print(f'my Favourite movie are:{favourite_movies}')

# 3.Write a Python program to display the first and last colors from the following list . color_list = ["Red","Green","White" ,"Black"]
color_list = ["Red", "Green", "White", "Black"]
print(f'{color_list[0]} is first color {color_list[-1]} is last color from the above list.')

# 4.Write a Python script to add a key to a dictionary
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
dict = {0: 10, 1: 20}
dict.update({2: 30})
print(f'updated dict:{dict}')

# 5. Write a Python program to calculate body mass index.
def calculate_BMI(height, weight):
    return round(weight / height ** 2)

height = float(input("Input your height (meters): "))
weight = float(input("Input your weight( Kgs): "))
print("Your body mass index is: ", calculate_BMI(height, weight))

# Additional Exercises:

#6. Guess a number game - between 1 to 9.
#Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

import random

random_num = random.randint(1, 9)
guess_number = int(input("Guess a number between 1 to 9: "))

while guess_number!=random_num:
    guess_number = int(input("sorry your guess is wrong,try guessing again a number between 1 to 9: "))
print("well guessed")


# 7 .Create a tuple with different data types
tuple_with_different_data_types= (1, 5.23, "Hello", False, ["apple", "banana", "cherry"])


# print(tuple_with_different_data_types)

# 8. Create a list of 5 city names and convert it into tuples.

city_names = ['copenhagen', 'Norway', 'sweden', 'Hyderabad', 'Mumbai']
tuplelist_of_cities = tuple(city_names)

print(f'City names as tuple:{tuplelist_of_cities}')

# 9.Remove duplicated from the list:
# a = [10,20,30,20,10,50,60,40,80,50,40] and store the values in the same list

a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
a = list(set(a))
print(f'List after Removing duplicates:{a}')


# 10. Accept a string from user and remove the characters which have odd index values of a given string and print them.
def remove_odd_string(str):
    final_str = ""
    for i, sample_char in enumerate(str):
        if i % 2 == 0:
            final_str +=sample_char
    return final_str

string = input("enter a string:")
print("characters which have odd index values of a given string are :", remove_odd_string(string))




