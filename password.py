import string
import random
length = int(input("Enter the length of the password: "))

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation
p = ""
for i in range(length) :
    p += random.choice(chars)

print("your password is " + p)



