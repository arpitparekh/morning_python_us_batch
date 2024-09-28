# single
# multi level
# hierarchical
# multiple
# hybrid

class A:
  def __init__(self): # default constructor
    print("A")

class B(A):
  def __init__(self):
    super().__init__()
    print("B")

class C(B):
  def __init__(self):
    super().__init__()
    print("C")


c = C()

class X:
  def __init__(self):
    print("X")

class Y:
  def __init__(self):
    super().__init__()
    print("Y")

class Z(X,Y):   # multiple inheritance
  def __init__(self):
    super().__init__()
    print("Z")

z = Z()


class P:
  def __init__(self):
    print("P")

class Q(P):
  def __init__(self):
    super().__init__()
    print("Q")

class R(P):
  def __init__(self):
    super().__init__()
    print("R")

q = Q()
r = R()
