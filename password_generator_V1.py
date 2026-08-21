import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
           ]

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*','(',')']

password = []

final_password = ""

print("Welcome to Password manager\n")
letter_count = int(input("Enter how many letters you want: "))
number_count = int(input("Enter how many numbers you want: "))
symbols_count = int(input("Enter how many symbols you want: "))

for i in range(1,letter_count+1):
    char = random.choice(letters)
    password += char

for i in range(1,number_count+1):
    char = random.choice(numbers)
    password += char

for i in range(1,number_count+1):
    char = random.choice(symbols)
    password += char    

random.shuffle(password)

for char in password:
    final_password += char


print("Your Password: ",final_password)