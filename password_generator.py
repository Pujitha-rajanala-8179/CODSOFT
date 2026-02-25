import random
import string

print("===PASSWORD GENERATOR ===")

length =int(input("Enter the length of the password: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(length):
    password += random.choice(characters)

print("Generated Password:",password)
