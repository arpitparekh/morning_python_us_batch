class A:
  def sum(self,a,b):
    return a+b
class B(A):
  def sum(self,a,b):
    return a+b

b = B()
print(b.sum(1,2))
# print(b.sum(1,2,3))

num = 12
num.add(12)
print(num)
