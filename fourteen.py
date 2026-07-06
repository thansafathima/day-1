# 26-06-26

# a = [11,13,14,15,16,17,18,19,20,12,15]
# convert it in to [11,13,14,15,16]
# [17,18,19,20,12,15]


# mid = len(a)//2
# c = []
# d = []
# for i in range(len(a)):
#     if i < mid:
#         c.append(a[i])
#     else:
#         d.append(a[i])
# print(c)
# print(d)



# print smallest and largest list from the list
# a = [11,1,100,-900,10,15,16]
# largest = 0
# smallest = 0
# for i in a:
#     if i > largest:
#         largest = i
#     if i < smallest:
#         smallest = i
# print(largest,smallest)



#FUNCTIONS
# ==========
# Function is a block of code which is executed when it is needed

# def functionname(<arguments>):
#     code to be executed

# def hello():
#     print("hello,good morning!!!!")

# hello()           #calling

# Arguments.  (values to be passed to a function)
# ==============
# def add2(a,b):    #former parameter
#     print(a+b)
# add2(10,20).  #actual parameter



# types of parameters
# 1.positional argumente
# 2.keyword arguments

# def add2(a,b):
#     print(a+b)
# add2(a=9,b=3).             keyword arguments

# default

def add2(a=0,b=0):
    print(a+b)
add2()        



