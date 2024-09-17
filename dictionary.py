# dictionary
# unordered
# mutable
# key value pair
# keys must be unique

my_dictionary={
  "Name":"Bascom",
  "Age":12,
  "Marks":[
    {
      "Maths":12
    }
  ],
  "isLogin":True,
}

numbers = {
  "one":1,
  "three":3,
  "five":5,
  "two":2
}

# sorted()

print(numbers.items())

print(sorted(numbers.values()))

# print(numbers.values())

print(sorted(numbers.items(),key=lambda x:x[1]))
