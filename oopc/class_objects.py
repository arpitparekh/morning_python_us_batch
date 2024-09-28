class MyClass:
  name = ""
  age = 0

obj = MyClass()
obj.name = "Bascom"
obj.age = 45

print(obj.name)
print(obj.age)

class AnotherClass:
  a = 0
  b = 0

  def assignValues(self,a,b):
    self.a = a
    self.b = b

  def displayValues(self):
    print(self.a)
    print(self.b)

obj2 = AnotherClass()
obj2.assignValues(12,13)
obj2.displayValues()

for x in [obj,obj2]:
  print(x)

class Student:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def display(self):
    print(self.name)
    print(self.age)

s = Student("Bascom",67)
s.display()

s1 = Student("Tops",45)
s1.display()

s1.name = "Jay"

del s1





