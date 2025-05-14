import random
import string
number = list(string.digits)
capital = list(string.ascii_uppercase)
lowers = list(string.ascii_lowercase)
specialchars = list(string.punctuation)

lenght = int(input("Enter Password Lenght:"))
numbers = input("Add numbers: (y/n): ")
capitals_characters = input("Add capitals characters: (y/n): ")
lowers_characters = input("Add lower characters: (y/n): ")
special_characters = input("Add special characters: (y/n): ")

password = []


if numbers == 'y' or numbers == 'Y':
    password = password + number
if capitals_characters == 'y' or special_characters == 'Y':
    password = password + capital
if lowers_characters == 'y' or lowers_characters == 'Y':
    password = password + lowers
if special_characters == 'y' or special_characters == 'Y':
    password = password + specialchars

else:
      print("Choosed nothing")

FINALPASSWORD = []
for i in range(lenght):
    temp = random.choice(password)
    FINALPASSWORD.append(temp)
FINALPASSWORD = ''.join(map(str,FINALPASSWORD))
print("Your random Passwords is: ",FINALPASSWORD)