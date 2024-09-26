# function is a block of code which only runs when it is called

# 4 types

# function name
# function paramater # is a datatype that we pass from the outside to a function
# function body
# function return

def myFunction():
  print("This is my Function")

myFunction()

def checkLeapYear(year):
  if year %4 ==0:
    print("Leap Year")
  else:
    print("Not Leap year")

checkLeapYear(2020)

def myValue():
  return 12.2

print(myValue())

result = 45 + myValue()

print(result)

def sum(a,b):
  return a+b

def mul(a,b):
  return a*b

print(sum( mul(2,3) , mul(3,4) ))

# lambda function
# function without any name
# lambda is a single line function

x =  lambda name : "Hello "+ name
print(x("Jay"))

# higher order function

def study(n):
  return lambda a : a*n

var = study(10)

print(var(12))


###############  lambda to a parameter #########

def master(a,b):
  print(a(1,2)+b(2,3))
  return a(b(4,5),b(6,7))

print(master(lambda x,y:x*y ,lambda p,q: p+q ))

#########################################


def fun():
  return 34


def student(a):
  print(a)

student(fun)
student(fun())

list2 = [fun,fun(),lambda x,y:x*y,x]

# pass function to the list

#############################################

print(range(20))

########################

def book(page1,page2,page3="Ending"):  # default value
  print(page1,page2,page3)

# named parameter

book(page1 = "Start", page2 = "Middle")

# *args (arbitary arguments)

def my_function(*args):
  print(args)
  my_list = list(args)
  # my_list =[*args]
  print(my_list)
  print(args[2])

my_function(1,2,3)


# **kwargs (arbitary keyword arguments)

def another_function(a,/,**args):
  print(args)

# another_function(a = 12,b = 13) # not allowed

# positional arguments only

def demo_function(a,b,/,c,d):
  print(a,b,c,d)

# demo_function(b = 12,a = 13)  # not allowed
demo_function(12,13,d = 55,c=33)

# keywords only arguments

def something(*args,a,b,c):
  print(args,a,b,c)

something(1,2,3,4,5,5,a = 12,c = 45,b = 12)


def jump(*,a,b):
  print(a,b)

jump(b = 12,a = 13)

#############3

def class_function(a,b,/,*,c,d):
  print(a,b,c,d)


class_function(10,20,c = 23,d = 56)
