# Generators
# it is lazy iterables


# def mydata:
#     yeild "one"
#     yeild "two"
#     yeild "three"
#     yeild "four"
#     yeild "five"
#     yeild "six"

# a = mydata()
# print(next(a))
# print(next(a))
# print(next(a))


# b = []
# i = 0
# while True:
#     b.append(i)
#     i = i + 1


# def inifinz():
#     i = 1
#     while True:
#         yeild i
#         i = i + 1


# infine_numbers = inifinz()
# print(infine_numbers)
# for i in infine_numbers:
#     print(i)


# import sys
# a = []
# for i in range(1,10000001):
#     a.append(i)

# def crore():
#     for i in range(1,10000001):
#         yield i
# b = crore

# print(sys.getsizeof(a))
# print(sys.getsizeof(b))


# map
# filter
# zip

# map
# maps each items in an iterable to a function
# map(fun,iterable)

# def square(z):
#     return z**2

z = lambda x : x**2
a =[1,2,3,4,5,6,7,8,9,10]
result = map(z,a)
print(list(result))