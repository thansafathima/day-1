# 23-06-2024
# set= collection of data
# it is declared by {}
# it is unorderd
# it is unindexed
# containing no duplicate values

# fruits = {"mango","orange","apple","watermelon","pineapple","grapes"}
# for i in fruits:
#     print(i)


# set is mutable
# union

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# print(a.union(b))       or
# print(a|b)


# intersection 

# a = {1,2,3,4,5}
# b = {4,5,6,7,8} 
# # print(a.intersection(b))           or
# print(a & b)

# difference

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# print(a - b)

# dictionary
# ===========
# key value paired datatype
# key:"value"
# it is also declared by {}
# dictionary have no index
# but it has keys
# it is mutable and dynamic
# # key:"value"


# userdata = {"name":"mohan","age":27,"location":"kochi"}
# print(type(userdata))

# # ans:it will print it as <class 'dict'>. if it is dictionary
#  if it is seen as key value pairs..python will take it as dictionary


# a = {1,2,3,4}
# print(type(a))
# now it will show as <class 'set'> because it is set


# a = {}
# print(type(a))
# the answer would be <class 'dict'> because if there is an empty set..it should be dictionary,because python always prioritise dictionary

# data = {}
# data["name" ] = "das"
# data["age"] = 27
# data["phone"] = 9935628851
# data["name"] = "priya"         dictionary keys are unique..so it will update the name to priya from das
# print(data)


# restrictions in dictionary

# keys are unique
# keys are immutable

# inbuilt functions

# a = {"name":"mohan","age":30,"location":"kochi"}
# print(a.get("name"))     or
# print(a["name"])
# print(a.keys())
# print(a.values())
# print(a.items())
# a.update({"age":34})
# print (a)

#pop
# ====

# a = {"name":"mohan","age":30,"location":"kochi"}
# a.pop("name")
# print(a)
# when you need to remove the last item from the list you have to use,popitem()
# a.popitem()
# print(a)

# when you have to clear everything we use,clear()

# a.clear()
# print(a)

# a = {"name":"mohan","age":30,"location":"kochi","email":"mohan123@gmail.com"}
# for i in a:
    # print(i)

# for i in a:
#     print(i,a[i])
# the answer will be:

# age 30
# location kochi
# email mohan123@gmail.com

# for i in a.keys():
#     print(i)

# the answer would be:
#  age
# location
# email


# for i in a.items():
#     print(i)

# the answer will be:
# ('name', 'mohan')
# ('age', 30)
# ('location', 'kochi')
# ('email', 'mohan123@gmail.com')

# we can modify it by;

# for i,j in a.items():
#     print(i,j)

# the answer will be:
# name mohan
# age 30
# location kochi
# email mohan123@gmail.com

#leetcode lemonade


#split

# a = "hello my name is kumar"
# b = a.split()
# print(b)
# ans:
# ['hello', 'my', 'name', 'is', 'kumar']


# b = a.split("a")
# print(b)
# the ans will be:
# ['hello my n', 'me is kum', 'r']


# instead of using split


a = "hello my name is kumar"
word = ""
b = []
for i in a:
    if i != '':
        word = word + i
    else:
        b.append(word)
        word = ""
b.append(word)
print(b)