list = [1,2,3,4,5,6,]
list2 = [1,2,3,4]
name = "Hello"
print(len(list))
print(len(list2))
print(len(name))

# you can  not polymorph a function in python

def add(a,b):
  print(a+b)

add(12,13)

def add(a,b,c=10):
  print(a+b+c)

add(1,2)
add(1,2,4)

