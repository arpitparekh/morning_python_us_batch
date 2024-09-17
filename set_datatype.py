# set
# uniue values
# unordered
# mutable
# no duplicate values

numbers = {1,2,4,5,4,6,4,4}
print(numbers)

other_numbers = set()  # set constructor is used to create an empty set

other_numbers = {}  # empty set or empty dictionary
print(type(other_numbers))

numbers.add(99)
print(numbers)

# numbers.remove(100)
numbers.discard(100)
numbers.clear()

numbers.update({1,2,3,4,9,99})
print(numbers)

# union
set1 = {1,2,3,4,5}
set2 = {4,5,6,7}

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)

# also use in

# set => frozenset

numbers = [12,4,5,4,3,5]
frozenNumbers = frozenset(numbers)
frozen = frozenset(set1)

print(frozenNumbers)
print(frozen)

print(len(frozen))
