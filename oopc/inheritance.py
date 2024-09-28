class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def running(self):
    print("running")


class Student(Person):

  def __init__(self,name,age):
    super().__init__(name,age)

  def display(self):
    print(self.name)
    print(self.age)
    super().running()

# when parent have a parameterized constructor child must have to class the parent class constrcutor

s = Student("Sugumar",67)
s.display()
