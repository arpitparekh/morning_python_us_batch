# f string
# ` {}`

import base64 as b4

a = 12

print(f"Value is {a}") # fstring

print(f"value is greater {"yes" if a>=12 else "no"}")


# 'hello'

print(" 'hello' ")

# "Hello"
print('  "Hello" ')

# "Hello"

print(" \"He\nllo\" ")

name = "Bascom Bridge"
print(name.center(20,"x"))

print(name.count("B"))

print(name.encode("UTF-8"))


print(b4.b64encode(name.encode()))

num = 2.3456

print("number is {number:.2f} and {number:.3f}".format(number=num))

number = 55

print("number is {:%} from python".format(345454455455))

characters = "%$%^&"
print(characters.isalnum())

name2 = "Barack Obama"
print(name2.partition("O"))
print(name2.split("O"))

