# list
# mutable
# ordered
# duplicate values

# tuple
# immutable # after defination
# ordered
# duplicate value

numbers = (1,1,2,3,45,6,5,3)
print(numbers)
print(type(numbers))

print(numbers[0])
# numbers[0] = 34   # not possible  # can not reassign
print(numbers)

lst_numbers =  list(numbers)
lst_numbers[0] = 0
numbers = tuple(lst_numbers)
print(numbers)

list = (8,9,8,9)

result_list = list + numbers
print(result_list)

(a,b,c,d) = list

print(a,b,c,d)

def universe(*ref):
  print(ref[0]["data"])
  pass

universe({"data":12},3434,34,67,7,5,4,[12])
