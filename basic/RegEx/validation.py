# email validation

# import re
#
# regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
#
# def isValid(email):
#     if re.fullmatch(regex, email):
#       print("Valid email")
#     else:
#       print("Invalid email")
#
# isValid('saliha123@mr.mm')

# 2.password validation

import re


# def password():
#     passwd = 'Geek12@'
#     reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
#
#     # compiling regex
#     pat = re.compile(reg)
#
#     # searching regex
#     mat = re.search(pat, passwd)
#
#     # validating conditions
#     if mat:
#         print("Password is valid.")
#     else:
#         print("Password invalid !!")
#
# password()

#3.  check whether the input string matches the regex pattern

# import re
#
# # compiling the pattern for alphanumeric string
# pat = re.compile(r"[A-Za-z0-9]+")
#
# # Prompts the user for input string
# test = input("Enter the string: ")
#
# # Checks whether the whole string matches the re.pattern or not
# if re.fullmatch(pat, test):
# 	print(f"'{test}' is an alphanumeric string!")
# else:
# 	print(f"'{test}' is NOT a alphanumeric string!")

# 4. ip adressess validation

# Python program to validate an Ip address

# re module provides support
# for regular expressions
import re

# Make a regular expression
# for validating an Ip-address
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
# Define a function for
# validate an Ip address
def check(Ip):
    # pass the regular expression
    # and the string in search() method
    if (re.search(regex, Ip)):
        print("Valid Ip address")
    else:
        print("Invalid Ip address")
# Driver Code
if __name__ == '__main__':
    # Enter the Ip address
    Ip = "192.168.0.1"
    # calling run function
    check(Ip)
    Ip = "110.234.52.124"
    check(Ip)
    Ip = "366.1.2.2"
    check(Ip)
