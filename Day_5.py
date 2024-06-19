#password generator that asks the user how many letters you want in your password

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


#ask for length of passowrd
password_length = int(input("How many letters would you like in your password?"))

#number of symbols
symbol_length = int(input("How many symbols"))

#number of numbers
numbers_length = int(input ("How many numbers"))

#number of letters
letters_length = int(password_length - symbol_length-numbers_length)

password_list = []
#select a random letters from the list using a for loop and random.choice () function
for char in range(1,letters_length+1):
    password_list.append(random.choice(letters))

for char in range(1,numbers_length+1):
    password_list.append(random.choice(numbers))

for char in range(1,symbol_length+1):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

new_password = ""
for char in password_list:
    new_password +=char

print(f"Your new password is {new_password}")