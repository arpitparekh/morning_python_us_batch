# how to take input from a user

# name = input("Enter your name: ")
# print(name)

# number = int(input("Enter a number: "))
# print(number)

marks = 34
# lst = list(marks)

# print(lst)

#########################################################
# if else elif ladder pass

num = 11

if num>13:
  pass
else:
  print("Small")

def display():
  pass

class Student:
  pass

if (num>12 and num<14):
  print("Big")
elif (True):
  print("Small")
else:
  print("Other")

# ? :  # no ternary operator
# check the greater number

a = 10
b = 20

result =  "Hello" if a<b else "Bye"  # one liner

# true if condition else
print(result)

# switch statements

# match and case

num = 34

match num:
  case 34:
    print("34")
  case 12:
    print("12")
  case _:                   # default
    print("Other")

# in in condition

data = [1,2,3,4,5,6,7,8,9,10]

if 33 in data:
  print("33")
else:
  print("Not Present")


dic = {
  12:13,
  1:"Bascom",
  2:"Bascom"
}

print(dic)

print(dic.values())

if 13 in dic.values():
  print("Present")
else:
  print("Not Present")
