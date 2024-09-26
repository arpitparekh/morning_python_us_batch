"""

1) find greatest from 3 numbers
2) fibonaccii  (0 1 1 2 3 5 8 13..)   # 5 input



"""
a = 12
b = 13
c = 15

if (a>b and a>c):
  print(a)
elif(b>c):
  print(b)
else:
  print(c)


x = 12
y = 13
z = 15
m = 16

if (x>y and x>z and x>m):
  print(x)
elif(y>z and y>m):
  print(y)
elif(z>m):
  print(z)
else:
  print(m)


#########################  (0 1 1 2 3 5 8 13..)

first ,second = 0,1

i = 1
while(i<=5):
  print(first)
  third = first+second
  first = second
  second = third
  i += 1
