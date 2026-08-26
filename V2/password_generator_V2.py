import random

uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*','(',')']

password = []

print("\n=== PASSWORD GENERATOR V2 ===")

password_length = int(input("Enter password length: "))
 
if password_length < 8:
    print("Password length must be at least 8 characters.")
    exit()

password += random.choice(uppercase)
password += random.choice(lowercase)
password += random.choice(numbers)
password += random.choice(symbols)

all_characters = uppercase + lowercase + numbers + symbols

for _ in range(password_length-4):
    password += random.choice(all_characters)

random.shuffle(password)

final_password = "".join(password)

print("Your password: ", final_password) 