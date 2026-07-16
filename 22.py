# 16 july 2026

# Decorators
# functions that enhances other functions

# def saymyname(fun):
#     def wrapper():
#         print("say my name")
#         fun()
#         print("you are right")
#     return wrapper
# @saymyname
# def add():
#     print("add 2 numbers")
# add()


# *args,**kwargs

# def num(*args):
#     print(args)
# num(10,70,60,55)




# def fullname(**kwargs):
#     print(kwargs)
# fullname(fname = "thansa",lname = "fathima")
# print()


# Time

# import time
# print(time.time())
# print(time.ctime())
# start = time.time()
# for i in range(1,11):
#     print(i)
#     time.sleep(1)
# stop = time.time()
# print("total time:",stop-start)


# import time
# def totaltime(fun):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         fun(*args,**kwargs)
#         stop = time.time()
#         print(f"total time :{stop-start}")
#     return wrapper

# @totaltime
# def myname(n):
#     for i in range(n):
#         print(i)
#         time.sleep(1)
# myname(5)


ans:

0
1
2
3
4
total time :5.012207269668579
