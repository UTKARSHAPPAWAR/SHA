import hashlib

# initializing string
str = input("Enter any string: ")

# String Encryption in SHA256
result = hashlib.sha256(str.encode())

print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())

print ("\r")

# String Encryption in SHA384
result = hashlib.sha384(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA384 is : ")
print(result.hexdigest())

print ("\r")
cdcd