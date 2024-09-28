list = [1,2,3,4,5,6]


myiter = iter(list)  # linked list
print(type(myiter))

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# class iterator

class Members:
  def __iter__(self):  # iter function will always return class current instance
    self.a = 1
    return self

  def __next__(self):
    if self.a <=5:
      num = self.a
      self.a += 1
      return num
    else:
      raise StopIteration

m = Members()

objIterator = iter(m)

print(next(objIterator))
print(next(objIterator))
print(next(objIterator))
print(next(objIterator))
print(next(objIterator))
print(next(objIterator))

class Student:
  def __init__(self,name,age):
    self.name = name
    self.age = age

objList = [Student("A",1),Student("B",2),Student("C",3)]

iterData = iter(objList)

print(next(iterData).name)
print(next(iterData).age)
print(next(iterData))

print(next(iterData))

