import re

password = input("Enter your password: ")

if (len(password) >= 8 and
    re.search("[A-Z]", password) and
    re.search("[a-z]", password) and
    re.search("[0-9]", password) and
    re.search("[@#$!&*]", password)):
    print("Password is Valid")
else:
    print("Password is Invalid")
