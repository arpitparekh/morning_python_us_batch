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

print(numbers["one"])

numbers["three"] = 12

print(numbers)

numbers.pop("three")
print(numbers)

numbers.update({"five":12})
print("updated",numbers)

numbers['six'] = 6
print(numbers)

list = [1,2,3,4,67,94323,51,2]
print(sorted(list))

# copy
dict1 = {"name":"Bascom","Address":"Ahmedabad","No_studnts":12}
dict2 = dict1.copy()
print(dict2)


# bytes number

b = bytes(12)
print(memoryview(b))

no = None    # null # just a reference variabel

