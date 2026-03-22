import random
import string

def create_password(len):
    chars = 'abcdefghijklmnopqrstuvwXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' + '1234567890' + '!@#$%^&*'
   
    password = ''.join(random.choice(chars) for _ in range(len))
    return password

len = int(input("Enter the Password length: "))

if(len<=0):
    print("Error: Invalid Input")
else:
    password = create_password(len)
    print("Password:", password)